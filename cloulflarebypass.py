#!/usr/bin/python
# Copyright (c) 2018 Twitter @Cyberddon - @iGlennio
#
#
#	CloudFlare ByPass - A função do script é listar todos os subdominio contra as proteções do CloudFlare
#	subdomainlist = ["ftp", "webmail"] << Você pode adicionar milhares de palavras para obter mais sucesso
#
#
#    Quero deixar claro que eu peguei o script no link https://github.com/cihanmehmet/cloudflarebypass
#    Fiz uma pequenas atualização na linguagem para executar o script na versão do python 3
#    Não me responsabilizo pelos uso do script. "apenas fiz as atualizações para estudos"
#	
#	Quem quiser melhorar o script, fiquem a vontade

import socket
import sys


subdomainlist = ["ftp", "cpanel", "whm", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog", "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator", "administration", "administ", "adm", "intranet", "extranet", "email", "downloads", "ssh", "owa","bbs", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5","shop", "api", "blogs", "test","mx1","cdn", "mysql", "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support", "web", "dev", "market", "marketing", "marketings", "admins", "login", "logins", "monitor", "log", "logs"]

class color:
    HEADER = '\033[0m'
	
logo = color.HEADER + '''
                                                                                             
                             **********************                               
                          *██████████████████████████(                         
                        (██████████████████████████████#                       
                      ,██████████████████████████████████*                     
                     (████████████████████████████████████(                    
                    #██████████████████████████████████████#                   
                   ██████████████████████████████████████████.                 
                     ,/#████████████████████████████████#(*.                   
                                .,,**********,,.                               
         ,(██████████#(*..                             .,/#█████████(,         
    .(███████████████████████████████████████████████████████████████████(.    
 *███████████████████████████████████████████████████████████████████████████( 
   .(█████████████████████████████████████████████████████████████████████#,   
       .(██████████████████████████████████████████████████████████████*       
            ,#████████████████████████████████████████████████████#,           
             *█     ████████████████████████████████████████     █*            
             .███████████████████████████████████████████████████.             
              (█/         *██████████████████████████#*.      /█/              
              .██.           ,███████████████████/           .█#               
               (██             .#█████████████(              #█                
                #██.             ,██████████(               #█.                
                 ███(              #███████.              *██.                 
                 .████#.            #█████.             /███                   
                   #██████/.         ████.          .(████(                    
                    /████████████##(/#██(,,,,/(#█████████*                     
                     .█████████████████████████████████#                       
                       /██████████████████████████████.                        
                         /██████████████████████████,                          
                           /██████████████████████.                            
                             *█████████████████#.                              
                               .#████████████/                                 
                                  .#██████/                                    

 ██████╗ ██╗   ██╗ ██████╗  ███████╗ ██████╗  ██████╗  ██████╗   ██████╗  ███╗   ██╗
██╔════╝ ╚██╗ ██╔╝ ██╔══██╗ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔══██╗ ██╔═══██╗ ████╗  ██║
██║       ╚████╔╝  ██████╔╝ █████╗   ██████╔╝ ██║  ██║ ██║  ██║ ██║   ██║ ██╔██╗ ██║
██║        ╚██╔╝   ██╔══██╗ ██╔══╝   ██╔══██╗ ██║  ██║ ██║  ██║ ██║   ██║ ██║╚██╗██║
╚██████╗    ██║    ██████╔╝ ███████╗ ██║  ██║ ██████╔╝ ██████╔╝ ╚██████╔╝ ██║ ╚████║
 ╚═════╝    ╚═╝    ╚═════╝  ╚══════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═════╝  ╚═╝  ╚═══╝
                                                                            								  
 
                                        Author: @iGlennio & @Cyberddon
                                        Version: 1.0
 
####################################### DISCLAIMER ########################################
| CloudFlare ByPass - A função do script é listar todos os subdominio com palavras chaves |
| Referencia do Script no link https://github.com/cihanmehmet/cloudflarebypass            |
| Fiz uma pequenas atualização na linguagem para executar o script na versão do python 3  |
|                                                                                         |
| Exemplo: python cloudflarebypass.py cyberddon.com.br                                    |
|                                                                                         |
###########################################################################################
                                                                                       
'''
print(logo)

host = input("Digite o dominio alvo: Exemplo:cyberddon.com = ")
for sublist in subdomainlist:
    try:
       hosts = str(sublist) + "." + str(host)
       showip = socket.gethostbyname(str(hosts))
       print ("[!] CloudFlare Bypass - @Cyberddon & @iGlennio "+str(showip)+' :| '+str(hosts))
    except:
            pass

