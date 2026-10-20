# Web Server Google Dorks

Google Dork queries for identifying web server types, versions, default pages, directory listings, and misconfigurations. These dorks are essential for the **reconnaissance phase** of penetration testing and C2 infrastructure hunting.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 32 |
| High | 87 |
| Medium | 74 |
| Low | 33 |
| Informational | 34 |

**Total: 260 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Query Reference

### Critical Risk

| Query | What It Finds |
|-------|---------------|
| `"Cisco Systems, Inc. All Rights Reserved." -cisco.com filetype:jsp` | Cisco JSP-based management interfaces outside cisco.com |
| `"PHP Credits" "Configuration" "PHP Core" ext:php inurl:info` | Exposed PHP info pages revealing full server configuration |
| `"index of /private" -site:net -site:com -site:org` | Directory listings of /private folders on non-standard TLDs |
| `"var miner = new CoinHive" intext:document.domain` | Websites with CoinHive cryptocurrency miner injected |
| `allintext:"Index Of" "sftp-config.json"` | Exposed SFTP configuration files in directory listings |
| `allinurl:".nsconfig" -sample -howto -tutorial` | Exposed Netscape/iPlanet server configuration files |
| `ext:php \| intitle:phpinfo "published by the PHP Group"` | Exposed phpinfo() pages revealing server configuration |
| `filetype:axd inurl:/elmah.axd` | Exposed ELMAH error log handlers in ASP.NET applications |
| `intext:"index of /" "Index of" access_log` | Exposed Apache access log files in directory listings |
| `intitle:"index of" "/homedir/etc/"` | Directory listings exposing user home directory config files |
| `intitle:"index of" "debug.log" OR "debug-log"` | Exposed debug log files in directory listings |
| `intitle:"index of" "docker.yml"` | Exposed Docker Compose configuration files |
| `intitle:"index of" AND inurl:magento AND inurl:/dev` | Magento development environments with directory listing |
| `intitle:"Welcome to WildFly" intext:"Administration Console"` | WildFly (JBoss) application server admin consoles |
| `inurl:"/app/kibana#"` | Exposed Kibana (Elasticsearch) dashboard instances |
| `inurl:"/domcfg.nsf" " Web Server Configuration"` | Lotus Domino web server configuration pages |
| `inurl:"/phpmyadmin/user_password.php` | phpMyAdmin password change pages (accessible instance) |
| `inurl:"/web-console/" intitle:"Administration Console"` | JBoss/WildFly web console administration interfaces |
| `inurl:":8088/cluster/apps"` | Exposed Hadoop YARN cluster management interfaces |
| `inurl:"id=*" & intext:"warning mysql_fetch_array()"` | Pages with SQL errors indicating potential SQL injection |
| `inurl:"web/database/selector"` | Odoo/OpenERP database selector pages |
| `inurl:/phpPgAdmin/browser.php` | Exposed phpPgAdmin PostgreSQL management interfaces |
| `inurl:2506/jana-admin` | Jana web server admin interfaces on port 2506 |
| `inurl:?XDEBUG_SESSION_START=phpstorm` | PHP applications with Xdebug remote debugging enabled |
| `inurl:CFIDE/adminapi` | ColdFusion admin API endpoints |
| `inurl:domcfg.nsf` | Lotus Domino server configuration databases |
| `intitle:"index of" "debian.cnf"` | Exposed MySQL Debian configuration files with credentials |
| `intitle:"index of" "debian.conf"` | Exposed Debian configuration files in directory listings |

### High Risk

| Query | What It Finds |
|-------|---------------|
| `"AnWeb/1.42h" intitle:index.of` | AnWeb 1.42h web servers with directory listing |
| `"JRun Web Server" intitle:index.of` | JRun servers with directory listing enabled |
| `"MaXX/3.1" intitle:index.of` | MaXX 3.1 web servers with directory listing |
| `"Microsoft-IIS/*" server at intitle:index.of` | Microsoft IIS servers with directory listing |
| `"CERN httpd 3.0B (VAX VMS)"` | Legacy CERN HTTP server signature on VAX VMS |
| `"Microsoft-IIS/4.0" intitle:index.of` | IIS 4.0 servers with directory listing (legacy) |
| `"Microsoft-IIS/6.0" intitle:index.of` | IIS 6.0 servers with directory listing |
| `"Novell, Inc" WEBACCESS Username Password "Version *.*" Copyright -inurl:help -guides\|guide` | Novell GroupWise WebAccess login portals |
| `"OmniHTTPd/2.10" intitle:index.of` | OmniHTTPd 2.10 servers with directory listing |
| `"OpenSA/1.0.4" intitle:index.of` | OpenSA 1.0.4 web servers with directory listing |
| `"RDServer Product information" \| inurl:"/rdagent.jsp"` | RDServer/Remote Desktop agent JSP interfaces |
| `"Wowza Streaming Engine 4 Developer Edition"` | Wowza Streaming Engine developer instances |
| `"httpd+ssl/kttd" * server at intitle:index.of` | httpd+ssl/kttd servers with directory listing |
| `(inurl:81-cobalt \| inurl:cgi-bin/.cobalt)` | Cobalt server administration interfaces |
| `-pub -pool intitle:"index of" "Served by" "Web Server"` | Web servers exposing directory listings |
| `allintext:"Powered by LionMax Software" "WWW File Share"` | LionMax WWW File Share Pro installations |
| `allintitle:"Pi-hole Admin Console"` | Exposed Pi-hole DNS sinkhole admin consoles |
| `fitweb-wwws * server at intitle:index.of` | FitWeb web servers with directory listing |
| `intext:"Healthy" + "Product model" + " Client IP" + "Ethernet"` | Exposed network device health/status pages |
| `intext:"Powered by Sentora" -github.com` | Sentora web hosting control panel installations |
| `intext:"SonarQube" + "by SonarSource SA." + "LGPL v3"` | Exposed SonarQube code quality analysis instances |
| `intext:Apache/2.2.29 (Unix) mod_ssl/2.2.29 \| intitle:"Index of /"` | Apache 2.2.29 servers with mod_ssl and directory listing |
| `intitle:"Accueil WAMPSERVER" intext:"Configuration Serveur"` | Exposed WAMP server dashboards with config |
| `intitle:"Apache Status" "Apache Server Status for"` | Exposed Apache server-status pages |
| `intitle:"Apache Status" \| intext:"Apache Server Status"` | Apache mod_status pages revealing server activity |
| `intitle:"BadBlue: the file-sharing web server anyone can use"` | BadBlue file-sharing web server (known vulnerabilities) |
| `intitle:"Current Network Status" "Nagios"` | Exposed Nagios network monitoring dashboards |
| `intitle:"Directory Listing, Index of /*/"` | Servers with directory listing via custom format |
| `intitle:"HFS" "Server Uptime" "Server time"` | HTTP File Server instances with file sharing |
| `intitle:"Index of *" mode links bytes last-changed name` | Directory listings with detailed file metadata |
| `intitle:"Index of /" "Proudly Served by Surftown at"` | Surftown-hosted servers with directory listing |
| `intitle:"Index of" "Apache/2.4.7 (Ubuntu) Server"` | Apache 2.4.7 on Ubuntu with directory listing |
| `intitle:"Index of" site:.gov intext:"Server at"` | Government servers with directory listing |
| `intitle:"Monsta ftp" intext:"Lock session to IP"` | Monsta FTP web-based FTP client installations |
| `intitle:"Open WebMail" "Open WebMail version (2.20\|2.21\|2.30) "` | Open WebMail with known vulnerable versions |
| `intitle:"Page rev */*/*" inurl:"admin` | Admin pages with revision timestamps |
| `intitle:"Server Backup Manager SE"` | Exposed Server Backup Manager SE interfaces |
| `intitle:"Shoutcast Administrator"` | SHOUTcast streaming server admin panels |
| `intitle:"WAMPSERVER homepage" "Server Configuration" "Apache Version"` | WAMP dashboards exposing server configuration |
| `intitle:"Welcome to IIS 4.0"` | Microsoft IIS 4.0 welcome pages (very legacy) |
| `intitle:"Welcome to JBoss"` | JBoss application server default pages |
| `intitle:"Welcome to Windows 2000 Internet Services"` | IIS on Windows 2000 (extremely legacy) |
| `intitle:"Welcome to Windows Small Business Server 2003"` | Windows SBS 2003 default pages |
| `intitle:"apache tomcat/" "Apache Tomcat examples"` | Tomcat servers with example apps exposed |
| `intitle:"apache tomcat/" + "Find additional important configuration information in:"` | Tomcat default pages with config guidance |
| `intitle:"index of" "Served by Sun-ONE"` | Sun ONE (iPlanet) servers with directory listing |
| `intitle:"index of" "powered by apache " "port 80"` | Apache servers with directory listing on port 80 |
| `intitle:"index of" "server at"` | Any web server with directory listing enabled |
| `intitle:"index of" site:.gov.in` | Indian government servers with directory listing |
| `intitle:"miniProxy"` | miniProxy web proxy installations |
| `intitle:"PHP Version" intext:"PHP Version"` | Exposed PHP version information pages |
| `intitle:"web server login" intext:"site ip"` | Web server login pages showing IP info |
| `intitle:Snoop Servlet` | Java Snoop Servlet debug pages |
| `inurl *:8080/login.php` | Login pages on port 8080 (dev/admin) |
| `inurl: /ftp intitle:"office"` | FTP directories containing office documents |
| `inurl:"WebPortal?bankid"` | Banking web portal applications |
| `inurl:"server-status" "Server Version: Apache/" "Server Built: " "Server uptime:" "Total accesses" "CPU Usage:"` | Detailed Apache server-status pages |
| `inurl:/config/device/wcd` | Web-based device configuration interfaces |
| `inurl:/php/info.php` | PHP info pages at common path |
| `inurl:/phpmyadmin/changelog.php -github -gitlab` | phpMyAdmin installations via changelog |
| `inurl:/server-status + "Server MPM:"` | Apache server-status with MPM info |
| `inurl:/uploads/affwp-debug.log` | Exposed AffiliateWP debug log files |
| `inurl:/xprober ext:php` | X Prober PHP server probe pages |
| `inurl:composer.json codeigniter -site:github.com` | Exposed Composer dependency files |
| `inurl:jsmol.php` | JSmol PHP proxy pages (SSRF risk) |
| `inurl:oraweb -site:oraweb.org` | Oracle web application server interfaces |
| `inurl:phpinfo.php intext:build 2600` | PHP info on Windows XP SP2 servers |
| `inurl:phpmyadmin/themes intext:"pmahomme"` | phpMyAdmin via exposed theme files |
| `inurl:phpsysinfo/index.php?disp=dynamic` | phpSysInfo pages with system details |
| `inurl:tech-support inurl:show Cisco` | Cisco device tech-support output pages |
| `inurl:wl.exe inurl:?SS1= intext:"Operating system:" -edu -gov -mil` | BEA WebLogic server pages with OS info |
| `Powered.by.RaidenHTTPD intitle:index.of` | RaidenHTTPD servers with directory listing |
| `XAMPP "inurl:xampp/index"` | XAMPP default dashboards (dev servers exposed) |
| `sEDWebserver * server +at intitle:index.of` | sEDWebserver with directory listing |
| `site:*/server-status intext:"Apache server status for"` | Apache server-status across all domains |
| `site:ftp.*.com "Web File Manager"` | Web-based FTP file manager interfaces |

### Medium Risk

| Query | What It Finds |
|-------|---------------|
| `"About Mac OS Personal Web Sharing"` | Mac OS X systems with Personal Web Sharing |
| `"I have been invoked by servletToJSP"` | Java servlet-to-JSP test/debug pages |
| `"Microsoft-IIS/5.0 server at"` | Microsoft IIS 5.0 servers via signature |
| `"NTRIP Caster Table Contents" "This is a SNIP NTRIP Caster"` | NTRIP GPS correction data services |
| `"Netware * Home" inurl:nav.html` | Novell NetWare web server home pages |
| `"Powered by phpBB" inurl:"index.php?s" OR inurl:"index.php?style"` | phpBB forum installations |
| `"Red Hat Secure/2.0"` | Red Hat Secure Server 2.0 |
| `"Red Hat Secure/3.0 server at"` | Red Hat Secure Server 3.0 |
| `"This server is operated by OpenX."` | OpenX ad server installations |
| `Coldbox \| contentbox \| commandbox "Powered by ContentBox"` | ColdFusion ContentBox CMS installations |
| `aboutprinter.shtml` | Network printer web interfaces |
| `allintitle:Netscape FastTrack Server Home Page` | Netscape FastTrack Server default pages |
| `ext:svc inurl:wsdl` | Exposed WCF/SOAP web service WSDL definitions |
| `filetype:asmx inurl:(_vti_bin\|api\|webservice)` | Exposed ASP.NET web service endpoints |
| `i_index.shtml Ready` | Network devices with status pages |
| `intext:"404 Object Not Found" Microsoft-IIS/5.0` | IIS 5.0 servers via custom 404 pages |
| `intext:"Powered by Abyss Web Server"` | Abyss Web Server installations |
| `intext:"Target Multicast Group" "beacon"` | Multicast beacon configuration pages |
| `intitle:"GlassFish Server - Server Running"` | Oracle GlassFish default pages |
| `intitle:"IPC@CHIP Infopage"` | IPC@CHIP embedded web server pages |
| `intitle:"Icecast Streaming Media Server"` | Icecast streaming server admin pages |
| `intitle:"Lists Web Service"` | Exposed SharePoint Lists Web Service |
| `intitle:"Object not found!" intext:"Apache/2.0.* (Linux/SuSE)"` | Apache 2.0 on SuSE Linux |
| `intitle:"Object not found" netware "apache 1.."` | Apache 1.x on NetWare |
| `intitle:"SOGo" site:webmail.*` | SOGo groupware/webmail installations |
| `intitle:"Shoutcast server" inurl:"/index.html" "SHOUTcast Server"` | SHOUTcast server status pages |
| `intitle:"Welcome To Your WebSTAR Home Page"` | WebSTAR web server default pages |
| `intitle:"Welcome to 602LAN SUITE *"` | 602LAN SUITE default pages |
| `intitle:"Welcome to the Advanced Extranet Server, ADVX!"` | ADVX Advanced Extranet Server pages |
| `intitle:AnswerBook2 inurl:ab2/ (inurl:8888 \| inurl:8889)` | Sun AnswerBook2 documentation servers |
| `intitle:Snap.Server inurl:Func=` | Snap.Server web server installations |
| `intitle:livezilla "Server Time"` | LiveZilla live chat server installations |
| `inurl:/Portal0000.htm` | Portal pages on embedded devices |
| `inurl:/_catalogs` | Exposed SharePoint catalog directories |
| `inurl:_vti_bin/Authentication.asmx` | SharePoint authentication web services |
| `inurl:nnls_brand.html OR inurl:nnls_nav.html` | Novell NetWare web server pages |
| `inurl:tests/mocks intext:autoloader` | Exposed test/mock directories in PHP apps |
| `site:vps-*.vps.ovh.net` | OVH VPS instances with default configs |
| `yaws.*.server.at` | Yaws (Erlang) web servers |

### Low Risk

| Query | What It Finds |
|-------|---------------|
| `"Powered by 123LogAnalyzer"` | Sites using 123LogAnalyzer analytics |
| `"Powered by BOINC"` | BOINC distributed computing servers |
| `"Powered by vShare"` | vShare video sharing platforms |
| `"Switch to table format" inurl:table\|plain` | Interfaces with switchable output formats |
| `"powered by" "shoutstats" hourly daily` | ShoutStats streaming statistics pages |
| `HTTP_USER_AGENT=Googlebot` | Pages displaying HTTP headers |
| `intext:" - 2019 Cott Systems, Inc."` | Cott Systems records management |
| `intext:"Powered by (Quantum \| Quantum CMS \| CMS)` | Quantum CMS installations |
| `intext:"Powered by GetSimple" -site:get-simple.info` | GetSimple CMS installations |
| `intext:"Powered by Nesta"` | Nesta CMS (Ruby-based) installations |
| `intext:"Powered by Typesetter"` | Typesetter CMS installations |
| `intitle:"300 multiple choices"` | HTTP 300 Multiple Choices responses |
| `intitle:"error 404" "From RFC 2068 "` | Custom 404 pages referencing RFC 2068 |
| `intitle:"nPerfServer"` | nPerf speed test servers |
| `intitle:"WATASHI SERVICE"` | WATASHI web service installations |
| `inurl:/_hcms/` | HCMS content management sites |
| `inurl:/javax.faces.resource/` | Java Server Faces applications |
| `inurl:/pub/ inurl:_ri_` | CMS publication/resource paths |
| `inurl:OrganizationChart.cc` | Exposed organization chart applications |
| `inurl:readme.md intext:"Laravel"` | Exposed Laravel README files |
| `inurl:readme.md intext:"typo3"` | Exposed TYPO3 README files |
| `inurl:readme.rst intext:"CodeIgniter"` | Exposed CodeIgniter README files |
| `inurl:user_guide intext:"CodeIgniter User Guide"` | Exposed CodeIgniter user guides |

### Informational

| Query | What It Finds |
|-------|---------------|
| `"Application Blocked!" "Google bot"` | WAF pages blocking Googlebot |
| `"Powered by"` | Generic powered-by footprints |
| `"Proudly created with Wix.com"` | Wix.com-built websites |
| `"seeing this instead" intitle:"test page for apache"` | Default Apache test pages |
| `intext:"Brought to you by eVetSites"` | eVetSites veterinary websites |
| `intext:"Welcome to CodeIgniter!"` | Default CodeIgniter welcome pages |
| `intitle: "Welcome to nginx!" + "Thank you for using nginx."` | Default nginx welcome pages |
| `intitle:"Apache HTTP Server" intitle:"documentation"` | Apache documentation pages |
| `intitle:"Apache2 Debian Default Page: It works"` | Default Apache2 on Debian |
| `intitle:"Apache2 Ubuntu Default Page: It works"` | Default Apache2 on Ubuntu |
| `intitle:"Domain Default page" "Parallels IP Holdings GmbH"` | Parallels Plesk default pages |
| `intitle:"IIS Windows Server" -inurl:"IIS Windows Server"` | Default IIS pages on Windows Server |
| `intitle:"Microsoft Internet Information Services 8" -IIS` | Default IIS 8 splash pages |
| `intitle:"Resin Default Home Page"` | Caucho Resin default pages |
| `intitle:"Success!" intext:"Your new web server is ready to use."` | Freshly deployed server pages |
| `intitle:"Sucuri WebSite Firewall - Access Denied"` | Sucuri WAF blocked access pages |
| `intitle:"Test Page for Apache"` | Apache test/default pages |
| `intitle:"Test Page for Apache" "It Worked!"` | Apache installation confirmation |
| `intitle:"Test Page for Apache" "It Worked!" "on this web"` | Detailed Apache test pages |
| `intitle:"Test Page for the HTTP Server on Fedora"` | Default Apache on Fedora Core |
| `intitle:"Test Page for the HTTP Server on Fedora"` | Default HTTP server on Fedora |
| `intitle:"Web Server's Default Page" intext:"hosting using Plesk" -www` | Plesk hosting default pages |
| `intitle:"Welcome To Xitami" -site:xitami.com` | Xitami web server default pages |
| `intitle:"Welcome to OpenResty!"` | Default OpenResty pages |
| `intitle:"Welcome to Your New Home Page!" "by the Debian release"` | Default Debian web server pages |
| `intitle:"Welcome to nginx!" intext:"Welcome to nginx on Debian!" intext:"Thank you for"` | Default nginx on Debian |
| `intitle:"Welcome" intext:"LiteSpeed Technologies, Inc. All Rights Reserved."` | LiteSpeed default welcome pages |
| `intitle:"welcome to mono xsp"` | Mono XSP web server default pages |
| `intitle:HTTP Server Test Page powered by CentOS` | Default HTTP server on CentOS |
| `intitle:Test Page for the Nginx HTTP Server on Fedora` | Default Nginx on Fedora |
| `inurl:/iisstart.htm intitle:"IIS7"` | Default IIS 7 start pages |
| `site:*/*.asp` | ASP pages across all domains |

## Example Usage

To find exposed Apache server-status pages:

```
intitle:"Apache Status" "Apache Server Status for"
```

This reveals servers with `mod_status` enabled, exposing:
- Current server uptime and load
- Active connections and request details
- Worker thread/process status
- Client IP addresses accessing the server

## Data Source

All queries in this collection are sourced from publicly available Google Dorking databases and security research. See the CSV file for the complete machine-readable dataset.
