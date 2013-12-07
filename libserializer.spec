Summary:	JFreeReport General Serialization Framework
Name:		libserializer
Version:	1.1.6
Release:	4
License:	LGPLv2+
Group:		Development/Java
Url:		http://reporting.pentaho.org
Source0:	http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Patch0:		%{name}-1.1.2-fix-build.patch
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	ant-contrib
BuildRequires:	ant-nodeps
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
BuildRequires:	libbase
Requires:	java
Requires:	jpackage-utils
Requires:	libbase

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom Java serialization handlers.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java 
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/libserializer-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

