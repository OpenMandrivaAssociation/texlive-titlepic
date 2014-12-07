# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/titlepic
# catalog-date 2009-11-10 08:50:14 +0100
# catalog-license pd
# catalog-version 1.1
Name:		texlive-titlepic
Version:	1.1
Release:	9
Summary:	Add picture to title page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlepic
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepic.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/titlepic/titlepic.sty
%doc %{_texmfdistdir}/doc/latex/titlepic/README
%doc %{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.pdf
%doc %{_texmfdistdir}/doc/latex/titlepic/titlepic-manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 756922
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719755
- texlive-titlepic
- texlive-titlepic
- texlive-titlepic

