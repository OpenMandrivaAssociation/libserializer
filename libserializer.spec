%{?_javapackages_macros:%_javapackages_macros}
%if 0%{?fedora}
%else
Epoch: 1
%endif
Name: libserializer
Version: 1.1.2
Release: 10.0%{?dist}
Summary: JFreeReport General Serialization Framework
License: LGPLv2+

#Original source: http://downloads.sourceforge.net/jfreereport/libserializer-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: libserializer-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org
BuildRequires: ant, ant-contrib, java-devel, jpackage-utils, libbase >= 1.1.2
Requires: java, jpackage-utils, libbase >= 1.1.2
BuildArch: noarch
Patch0: libserializer-1.1.2.build.patch

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom java serialization handlers.

%package javadoc
Summary: Javadoc for %{name}
%if 0%{?fedora}
Requires: %{name} = %{version}-%{release}
%else
Requires: %{name} = %{EVRD}
%endif
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/libserializer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 06 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1.2-10
- ant-nodeps is dropped from ant-1.9.0-2 build in rawhide
- Drop buildroot, %%clean, %%defattr and removal of buildroot in %%install

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.2-7
- repack source to remove bundled multi-license .jars

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> - 1.1.2-4
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 Caolán McNamara <caolanm@redhat.com> 1.1.2-2
- fix up source-code download foo

* Fri Nov 20 2009 Caolán McNamara <caolanm@redhat.com> 1.1.2-1
- initial fedora import
