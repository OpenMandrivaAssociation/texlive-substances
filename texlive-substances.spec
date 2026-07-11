%global tl_name substances
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2a
Release:	%{tl_revision}.1
Summary:	A database of chemicals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/substances
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/substances.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/substances.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to create a database-like file that
contains data of various chemicals. These data may be retrieved in the
document; an index of the chemicals mentioned in the document can be
created..

