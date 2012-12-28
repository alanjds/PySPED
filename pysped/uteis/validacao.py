#coding: utf-8

from lxml import etree
import logging
from logging import getLogger

log = getLogger(__name__)


class Validador(object):
    def __init__(self, arquivo_esquema):
        self.arquivo_esquema = arquivo_esquema
        #raise NotImplementedError()
        
    def validar(self, xml):
        xml_tree = etree.fromstring(xml.encode('utf-8'))
        
        log.info(u'Arquivo de schema: %s', self.arquivo_esquema)
        esquema = etree.XMLSchema(etree.parse(self.arquivo_esquema))
        #esquema.assertValid(etree.fromstring(xml))

        if not esquema.validate(xml_tree):
            erros = esquema.error_log
            last_error = unicode(erros.last_error)
            log.info(u'Erro: %s', last_error)
            if log.level == logging.DEBUG:
                # Exibe as linhas que geraram o erro, numeradas e indentadas
                for nr, line in enumerate(
                        etree.tounicode(
                            xml_tree,
                            pretty_print=True
                        ).split('\n')):
                    log.debug(u'%s %s', nr+1, line)
                    #raise AssertionError(unicode(schema.error_log))
                log.debug(u'Erro: %s', last_error)
            
            log.info(u'XML não validou no esquema "%s"', self.arquivo_esquema)
        else:
            erros = []

        return erros


def validar(xml, arquivo_esquema):
    return Validador(arquivo_esquema).validar(xml)


if __name__ == '__main__':
    # Usa-se assim:
    
    #from pysped.uteis.validacao import validar
    
    #import logging
    #logging.basicConfig(level=logging.INFO)
    #logging.getLogger('pysped.uteis.validacao').setLevel(logging.DEBUG)
    
    #res = validar(n.xml, n.caminho_esquema+n.arquivo_esquema)
    pass
