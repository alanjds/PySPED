# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import abspath, dirname
from pysped.xml_sped.certificado import Certificado

FILE_DIR = abspath(dirname(__file__))

if __name__ == '__main__':
    certificado = Certificado()
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    certificado.arquivo = open(FILE_DIR+'/certificado_caminho.txt').read().strip()
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    certificado.senha = open(FILE_DIR+'/certificado_senha.txt').read().strip()
    
    cte_xml = open(FILE_DIR+'/xml_teste/000000246.xml', 'r').read()
    xml_assinado = certificado.assina_xml(cte_xml)

    print xml_assinado

    # Para uso posterior
    arquivo_assinado = open(FILE_DIR+'/xml_teste/000000246_assinado.xml', 'w').write(xml_assinado)