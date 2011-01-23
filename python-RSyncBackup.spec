
%define 	module	RSyncBackup

Summary:	Python module for perform automatic backups using the rsync command
Summary(pl.UTF-8):	Moduł Pythona umożliwiający wykonywanie automatycznych archiwizacji przy pomocy komendy rsync
Name:		python-%{module}
Version:	1.3
Release:	3
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.owlfish.com/software/utils/RSyncBackup/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	b9fbf6a37b8634884dea330770948ac9
URL:		http://www.owlfish.com/software/utils/RSyncBackup/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.3
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSyncBackup is the Python module that allows automatic backups using
the rsync command. rsync has many different uses but is particularly
suitable for performng backups from one form of online storage to
another, either over a network or on a local machine with multiple
drives.

%description -l pl.UTF-8
RSyncBackup jest modułem Pythona pozwalającym na wykonywanie
automatycznych archiwizacji. rsync posiada wprawdzie wiele innych
możliwości, ale szczególnie użyteczny jest do przeprowadzania
archiwizacji między wieloma urządzeniami, zarówno poprzez sieć jak i
na lokalnej maszynie między różnymi dyskami.

%package doc
Summary:	Documentation for RSyncBackup module
Summary(pl.UTF-8):	Dokumentacja do modułu RSyncBackup
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for RSyncBackup Python
module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona RSyncBackup.

%package examples
Summary:	Examples for RSyncBackup module
Summary(pl.UTF-8):	Przykłady do modułu RSyncBackup
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for RSyncBackup Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona RSyncBackup.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%{py_sitescriptdir}/RSyncBackup.py[oc]

%files doc
%defattr(644,root,root,755)
%doc documentation/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
