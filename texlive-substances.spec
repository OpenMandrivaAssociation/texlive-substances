# revision 27182
# category Package
# catalog-ctan /macros/latex/contrib/substances
# catalog-date 2012-07-22 22:37:06 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-substances
Version:	0.1
Release:	5
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
%{_texmfdistdir}/tex/latex/substances/substances-default.def
%{_texmfdistdir}/tex/latex/substances/substances.sty
%doc %{_texmfdistdir}/doc/latex/substances/README
%doc %{_texmfdistdir}/doc/latex/substances/substances-examples.sub
%doc %{_texmfdistdir}/doc/latex/substances/substances_en.pdf
%doc %{_texmfdistdir}/doc/latex/substances/substances_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 813777
- Import texlive-substances
- Import texlive-substances

