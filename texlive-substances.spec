Name:		texlive-substances
Version:	0.2a
Release:	2
Summary:	A database of chemicals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/substances
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substances.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/substances.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to create a database-like file
that contains data of various chemicals. These data may be
retrieved in the document; an index of the chemicals mentioned
in the document can be created..

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/substances
%doc %{_texmfdistdir}/doc/latex/substances

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
