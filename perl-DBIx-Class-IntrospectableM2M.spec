#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DBIx
%define	pnam	Class-IntrospectableM2M
Summary:	DBIx::Class::IntrospectableM2M - Introspect many-to-many shortcuts
#Summary(pl.UTF-8):	
Name:		perl-DBIx-Class-IntrospectableM2M
Version:	0.001001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c05959fdb632062ec827ec0c7335eae
URL:		http://search.cpan.org/dist/DBIx-Class-IntrospectableM2M/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBIx-Class
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Because the many-to-many relationships are not real relationships, they can not
be introspected with DBIx::Class. Many-to-many relationships are actually just
a collection of convenience methods installed to bridge two relationships.
This DBIx::Class component can be used to store all relevant information
about these non-relationships so they can later be introspected and examined.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DBIx/Class/*.pm
%{_mandir}/man3/*
