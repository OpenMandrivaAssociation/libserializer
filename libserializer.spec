Name:           libserializer
Version:        1.1.6
Release:        %mkrel 5
Summary:        JFreeReport General Serialization Framework
License:        LGPLv2+
Group:          Development/Java
URL:            http://reporting.pentaho.org
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Patch0:         %{name}-1.1.2-fix-build.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  ant-nodeps
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
Requires:       java
Requires:       jpackage-utils
Requires:       libbase
BuildArch:      noarch

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom Java serialization handlers.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation 
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

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
%defattr(0644,root,root,0755)
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-5.mga3
+ Revision: 358140
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 1.1.6-4.mga3
+ Revision: 305451
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 1.1.6-3.mga2
+ Revision: 198940
- rebuild against new libbase-1.1.6

* Sat Jan 21 2012 kamil <kamil> 1.1.6-2.mga2
+ Revision: 198915
- drop gcj support

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198909
- new version 1.1.6
- clean .spec
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.2-4.mga1
+ Revision: 74301
- Really build without gcj

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.2-3.mga1
+ Revision: 74284
- Build without gcj

* Mon Jan 24 2011 dmorgan <dmorgan> 1.1.2-2.mga1
+ Revision: 35769
- Adapt to mageia
- imported package libserializer

