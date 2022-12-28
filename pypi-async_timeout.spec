#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-async_timeout
Version  : 4.0.2
Release  : 43
URL      : https://files.pythonhosted.org/packages/54/6e/9678f7b2993537452710ffb1750c62d2c26df438aa621ad5fa9d1507a43a/async-timeout-4.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/54/6e/9678f7b2993537452710ffb1750c62d2c26df438aa621ad5fa9d1507a43a/async-timeout-4.0.2.tar.gz
Summary  : Timeout context manager for asyncio programs
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-async_timeout-license = %{version}-%{release}
Requires: pypi-async_timeout-python = %{version}-%{release}
Requires: pypi-async_timeout-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
async-timeout
=============
.. image:: https://travis-ci.com/aio-libs/async-timeout.svg?branch=master
:target: https://travis-ci.com/aio-libs/async-timeout
.. image:: https://codecov.io/gh/aio-libs/async-timeout/branch/master/graph/badge.svg
:target: https://codecov.io/gh/aio-libs/async-timeout
.. image:: https://img.shields.io/pypi/v/async-timeout.svg
:target: https://pypi.python.org/pypi/async-timeout
.. image:: https://badges.gitter.im/Join%20Chat.svg
:target: https://gitter.im/aio-libs/Lobby
:alt: Chat on Gitter

%package license
Summary: license components for the pypi-async_timeout package.
Group: Default

%description license
license components for the pypi-async_timeout package.


%package python
Summary: python components for the pypi-async_timeout package.
Group: Default
Requires: pypi-async_timeout-python3 = %{version}-%{release}

%description python
python components for the pypi-async_timeout package.


%package python3
Summary: python3 components for the pypi-async_timeout package.
Group: Default
Requires: python3-core
Provides: pypi(async_timeout)

%description python3
python3 components for the pypi-async_timeout package.


%prep
%setup -q -n async-timeout-4.0.2
cd %{_builddir}/async-timeout-4.0.2
pushd ..
cp -a async-timeout-4.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672256595
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-async_timeout
cp %{_builddir}/async-timeout-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-async_timeout/2a8f799cf5d5f9ad7c402c17b6a460580bb806d2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-async_timeout/2a8f799cf5d5f9ad7c402c17b6a460580bb806d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
