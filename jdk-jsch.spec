Name     : jdk-jsch
Version  : 0.1.54
Release  : 3
URL      : http://download.sourceforge.net/sourceforge/jsch/jsch-0.1.54.zip
Source0  : http://download.sourceforge.net/sourceforge/jsch/jsch-0.1.54.zip
Source1  : MANIFEST.MF
Source2  : plugin.properties
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-jzlib
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-source-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-sonatype-oss-parent
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
JSch
Java Secure Channel
by ymnk@jcraft.com, JCraft,Inc.
http://www.jcraft.com/jsch/

%prep
%setup -q -n jsch-0.1.54

python3 /usr/share/java-utils/mvn_file.py : jsch
python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove   pom:project/pom:build/pom:extensions
python3 /usr/share/java-utils/pom_editor.py pom_xpath_set      pom:project/pom:version 0.1.54

%build
python3 /usr/share/java-utils/mvn_build.py

mkdir META-INF
cp %{SOURCE2} META-INF
cp %{SOURCE2} plugin.properties
touch META-INF/MANIFEST.MF
touch plugin.properties
zip target/jsch-0.1.54.jar META-INF/MANIFEST.MF
zip target/jsch-0.1.54.jar plugin.properties

%install
xmvn-install  -R .xmvn-reactor -n jsch -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/jsch.jar
/usr/share/maven-metadata/jsch.xml
/usr/share/maven-poms/jsch.pom
