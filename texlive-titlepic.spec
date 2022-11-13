Name:		texlive-titlepic
Version:	43497
Release:	1
Summary:	Add picture to title page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlepic
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to place a picture on the title page
(cover page) of a LaTeX document. Example of usage:
\usepackage[cc]{titlepic} \usepackage{graphicx}
\titlepic{\includegraphics[width=\textwidth]{picture.png}} The
package currently only works with the document classes article,
report and book.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titlepic
%doc %{_texmfdistdir}/doc/latex/titlepic

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
