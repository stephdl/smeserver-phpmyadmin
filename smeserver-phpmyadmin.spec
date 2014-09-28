# $Id: smeserver-phpmyadmin.spec,v 1.8 2013/06/23 00:20:28 unnilennium Exp $
# Authority: darrellmay
# Name: Darrell May

Summary: phpMyAdmin for SME Server 
%define name smeserver-phpmyadmin
Name: %{name}
%define version 4.0.10.2
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Mitel/addon
Source: %{name}-%{version}.tar.gz
URL: http://www.phpmyadmin.net/ 
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: phpMyAdmin >= 4.0.10.1
Requires: e-smith-release >= 9.0
Obsoletes: phpmyadmin,phpMyAdmin3
BuildRequires: e-smith-devtools
Obsoletes: e-smith-phpmyadmin
Obsoletes: smeserver-phpmyadmin <= 3.5.2.2-1
Obsoletes: smeserver-phpmyadmin-multiuser

%description
Implementation of phpMyAdmin for SME Server.
Access with admin username/password via: https://yourdomain/phpmyadmin.

%changelog
* Sun Sep 28 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.0.10.2-1.sme
- added an event template on 'phpmyadmin-update'
- added a phpmyadmin.sql db to save settings in db
- new cool features (bookmarktable,relation,userconfig,table_info,column_info,history,
- recent,table_uiprefs,tracking,table_coords,pdf_pages,designer_coords)
- the http://url/setup page is now forbidden by apache
- a db 'status' exists now to disable simply phpmyadmin in httpd.conf
- removed the openbasedir of /tmp to /var/lib/phpMyAdmin/tmp
 
* Wed Sep 24 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.0.10.1-1.sme
- add memory value up to 500M
- add php upload/post up to 100M
- add session.use_trans_sid 0
- directory 'scripts' removed of httpd templates
- VersionCheck is off now

* Mon May 19 2014 stephane de labrusse <stephdl@de-labrusse.fr> 3.5.8.2-2
-first release to sme9
-added an event template on 'signal-event console-save'
 
* Sat Jun 22 2013 JP Pialasse <tests@pialasse.com> 3.5.2.2-6
- Obsolete multiuser [SME: 7685]

* Tue Jun 18 2013 JP Pialasse <tests@pialasse.com> 3.5.2.2-5
- added full 3.5 configuration to avoid errors [SME: 7153] [SME: 7194]
- incorporated multiuser contrib in this package [SME: 7628 7627 ]
- increased security [SME: 5007]
- configext.patch
- release bump to 4 to fix spec file
- patch1 to fix config.inc.php syntax error

* Thu Aug 06 2012 JP Pialasse  aka Unnilennium  <tests@pialasse.com> 3.5.2.2-2
- first version for SME 8
- adaptation for phpMyAdmin3 3.5.2.2

* Thu May 15 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 2.11.1.2-3
- Protect sensible data and prevent access error by setting 
  proper permissions to config.inc.php template [SME: 4343]

* Wed May 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl>
- Converted RPM to be an integrational RPM [SME: 4298]:
- Convert and move templates to RPMForge (Dag) install location [SME: 4339]
- Automatically expand phpmyadmin configuation file (config.php.inc) [SME: 4340]
- Remove PHPMyAdmin core [SME: 4341]

* Mon Apr 21 2008 Shad L. Lords <slords@mail.com>
- Prep for import into buildsys
- Clean up spec

* Fri Oct 19 2007 Darrell May <dmay@myezserver.com>
- accounts and configuration db phpmyadmin defaults added
- default access restricted to private (private|public)
- phpMyAdmin 2.11.1.2
- [ 2.11.1.2-0]
* Fri Mar 09 2007 Darrell May <dmay@myezserver.com>
- phpMyAdmin 2.10.0.2
- [ 2.10.0.2-0]
* Thu Oct 12 2006 Darrell May <dmay@myezserver.com>
- phpMyAdmin 2.9.0.2
- [ 2.9.0.2-0]
* Thu Dec 15 2005 Darrell May <dmay@myezserver.com>
- phpMyAdmin 2.6.4-pl4
- [ 2.6.4-pl4]
* Fri Apr 22 2005 Darrell May <dmay@myezserver.com>
- added support for SME 7.x
- [ 2.6.2-2]
* Mon Apr 18 2005 Darrell May <dmay@myezserver.com>
- Release 2.6.2 of phpMyAdmin
- change rpm name to smeserver-phpmyadmin
- change install dir to /opt/phpmyadmin
- [ 2.6.2-1]

%prep
%setup

%build
%{__mkdir_p} root/var/lib/phpMyAdmin/tmp
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
rm -f %{name}-%{version}-filelist
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist  \
    --dir /var/lib/phpMyAdmin/tmp 'attr(0770,root,www)' \
    $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc CHANGELOG.git" >> %{name}-%{version}-filelist
echo "%doc phpmyadmin.sql" >> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean 
rm -rf $RPM_BUILD_ROOT

