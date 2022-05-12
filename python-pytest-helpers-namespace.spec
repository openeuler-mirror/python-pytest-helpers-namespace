%global _empty_manifest_terminate_build 0
Name:		python-pytest-helpers-namespace
Version:	2021.4.29
Release:	2
Summary:	Pytest Helpers Namespace Plugin
License:	Apache Software License 2.0
URL:		https://github.com/saltstack/pytest-helpers-namespace
Source0:	pytest-helpers-namespace-%{version}.tar.gz
BuildArch:	noarch
Provides:	python-pytest-helpers-namespace

Requires:	python3-pytest
Requires:	python3-sphinx
Requires:	python3-sphinx-material-saltstack
Requires:	python3-sphinx-prompt
Requires:	python3-sphinxcontrib-spelling
Requires:	python3-pylint
Requires:	python3-saltpylint
Requires:	python3-pyenchant
Requires:	python3-black
Requires:	python3-reorder-python-imports

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
BuildRequires:	python3-wheel
BuildRequires:  python3-setuptools-declarative-requirements
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-toml
%description
This plugin does not provide any helpers to pytest, it does, however, provide a helpers namespace in pytest 
which enables you to register helper functions in your conftest.py to be used within your tests 
without having to import them.

%prep
%autosetup -n pytest-helpers-namespace-%{version}

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> filelist.lst
fi
popd
mv %{buildroot}/filelist.lst .

%files -f filelist.lst
%dir %{python3_sitelib}/*
%{_docdir}/*

%changelog
* Wed May 18 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn>
- add necessary BuildRequires

* Tue Jun 29 2021 Python_Bot <Python_Bot@openeuler.org> - 2021.4.29-1
- Package Spec generated
