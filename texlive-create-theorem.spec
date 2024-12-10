Name:		texlive-create-theorem
Version:	72830
Release:	1
Summary:	Multilingual support for theorem-like environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/create-theorem
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/create-theorem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/create-theorem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for naming, initializing and
configuring theorem-like environments. These commands have
key-value based interfaces and are especially useful in
multilingual documents, allowing the easy declaration of
theorem-like environments that can automatically adapt to the
language settings.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/create-theorem
%doc %{_texmfdistdir}/doc/latex/create-theorem

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
