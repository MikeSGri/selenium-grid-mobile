FROM ubuntu:bionic-20200311

ENV DEBIAN_FRONTEND=noninteractive

ENV SDK_VERSION=sdk-tools-linux-3859397 \
    ANDROID_BUILD_TOOLS_VERSION=31.0.0 \
    APPIUM_VERSION=1.21.0 \
    ATD_VERSION=1.2

#=============
# Set WORKDIR
#=============
WORKDIR /root

#==================
# General Packages
#------------------
# openjdk-8-jdk
#   Java
# ca-certificates
#   SSL client
# tzdata
#   Timezone
# zip
#   Make a zip file
# unzip
#   Unzip zip file
# curl
#   Transfer data from or to a server
# wget
#   Network downloader
# libqt5webkit5
#   Web content engine (Fix issue in Android)
# libgconf-2-4
#   Required package for chrome and chromedriver to run on Linux
# xvfb
#   X virtual framebuffer
# gnupg
#   Encryption software. It is needed for nodejs
# salt-minion
#   Infrastructure management (client-side)
#==================
RUN apt-get -qqy update && \
    apt-get -qqy --no-install-recommends install \
    openjdk-8-jdk \
    ca-certificates \
    tzdata \
    zip \
    unzip \
    curl \
    wget \
    libqt5webkit5 \
    libgconf-2-4 \
    xvfb \
    gnupg \
    salt-minion \
    git clone https://github.com/appium/appium-geckodriver.git \
  && rm -rf /var/lib/apt/lists/*

#===============
# Set JAVA_HOME
#===============
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre" \
    PATH=$PATH:$JAVA_HOME/bin

#=====================
# Install Android SDK
#=====================
ARG ANDROID_PLATFORM_VERSION="android-25"
ENV ANDROID_HOME=/root

RUN wget -O tools.zip https://dl.google.com/android/repository/${SDK_VERSION}.zip && \
    unzip tools.zip && rm tools.zip && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME

ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin

# https://askubuntu.com/questions/885658/android-sdk-repositories-cfg-could-not-be-loaded
RUN mkdir -p ~/.android && \
    touch ~/.android/repositories.cfg && \
    echo y | sdkmanager "platform-tools" && \
    echo y | sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION" && \
    echo y | sdkmanager "platforms;$ANDROID_PLATFORM_VERSION"

ENV PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools

#====================================
# Install latest nodejs, npm, appium
# Using this workaround to install Appium -> https://github.com/appium/appium/issues/10020 -> Please remove this workaround asap
#====================================
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash && \
    apt-get -qqy install nodejs && \
    npm install -g appium@${APPIUM_VERSION} --unsafe-perm=true --allow-root --chromedriver_version="94.0.4606.41" && \
    exit 0 && \
    npm cache clean && \
    apt-get remove --purge -y npm && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean

#================================
# APPIUM Test Distribution (ATD)
#================================
RUN wget -nv -O RemoteAppiumManager.jar "https://github.com/AppiumTestDistribution/ATD-Remote/releases/download/${ATD_VERSION}/RemoteAppiumManager-${ATD_VERSION}.jar"

#==================================
# Fix Issue with timezone mismatch
#==================================
ENV TZ="US/Pacific"
RUN echo "${TZ}" > /etc/timezone

#installing sdkmanager and accepting licenses
ENV ANDROID_VERSION=25 \
     ANDROID_BUILD_TOOLS_VERSION=26.0.2
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --update
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses && yes | $ANDROID_HOME/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
    "platforms;android-${ANDROID_VERSION}" \
    "platform-tools"

#RUN apt-get install -y maven
    #RUN apt-get install -y ant

RUN sdkmanager "platforms;android-16" "platforms;android-19"
RUN npm install


#====================================================
# Scripts to run appium and connect to Selenium Grid
#====================================================
COPY entry_point.sh \
     generate_config.sh \
     package.json \
     /root/


#COPY samsung.json /root/nodeconfig.json
RUN chmod +x /root/entry_point.sh && \
    chmod +x /root/generate_config.sh 

# connecting appium
ENV CONNECT_TO_GRID=false
ENV CUSTOM_NODE_CONFIG=false
ENV RELAXED_SECURITY=true
ENV CHROMEDRIVER_AUTODOWNLOAD=true
#===============
# Expose Ports
#---------------
# 4723
#   Appium port
# 4567
#   ATD port
#===============
EXPOSE 4567
#========================================
# Run xvfb and appium server
#========================================

CMD /root/entry_point.sh   

