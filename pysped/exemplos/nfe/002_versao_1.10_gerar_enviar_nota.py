# -*- coding: utf-8 -*-

from pysped.nfe import ProcessadorNFe
from pysped.nfe.webservices_flags import *
from pysped.nfe.manual_300 import *
from datetime import datetime
from os.path import abspath, dirname

FILE_DIR = abspath(dirname(__file__))

if __name__ == '__main__':
    p = ProcessadorNFe()
    p.versao              = u'1.10'
    p.estado              = u'SP'
    # arquivo 'certificado_caminho.txt' deve conter o caminho para o 'certificado.pfx'
    p.certificado.arquivo = open(FILE_DIR+'/certificado_caminho.txt').read().strip()
    # arquivo 'certificado_senha.txt' deve conter a senha para o 'certificado.pfx'
    p.certificado.senha   = open(FILE_DIR+'/certificado_senha.txt').read().strip()
    p.salvar_arquivos     = True
    p.contingencia_SCAN   = False
    p.caminho = u'' 
    
    #
    # Instancia uma NF-e
    #
    n = NFe_110()

    #
    # Identificação da NF-e
    #
    n.infNFe.ide.cUF.valor     = UF_CODIGO[u'SP']
    n.infNFe.ide.natOp.valor   = u'Venda de produto do estabelecimento'
    n.infNFe.ide.indPag.valor  = 2
    n.infNFe.ide.serie.valor   = 101
    n.infNFe.ide.nNF.valor     = 29
    n.infNFe.ide.dEmi.valor    = datetime(2010, 12, 12)
    n.infNFe.ide.dSaiEnt.valor = datetime(2010, 12, 12)
    n.infNFe.ide.cMunFG.valor  = 3513801
    n.infNFe.ide.tpImp.valor   = 1
    n.infNFe.ide.tpEmis.valor  = 1
    n.infNFe.ide.indPag.valor  = 1
    n.infNFe.ide.finNFe.valor  = 1
    n.infNFe.ide.procEmi.valor = 0
    n.infNFe.ide.verProc.valor = u'PySPED NFe (github)'
    
    #
    # Emitente
    #
    n.infNFe.emit.CNPJ.valor  = p.certificado.proprietario_cnpj #u'11111111111111'
    n.infNFe.emit.xNome.valor = p.certificado.proprietario_nome #u'Razão Social Ltda. EPP'
    n.infNFe.emit.xFant.valor = u'Nome Fantasia'
    n.infNFe.emit.enderEmit.xLgr.valor    = u'R. Ibiúna'
    n.infNFe.emit.enderEmit.nro.valor     = u'729'
    n.infNFe.emit.enderEmit.xCpl.valor    = u'sala 3'
    n.infNFe.emit.enderEmit.xBairro.valor = u'Jd. Morumbi'
    n.infNFe.emit.enderEmit.cMun.valor    = u'3552205'
    n.infNFe.emit.enderEmit.xMun.valor    = u'Sorocaba'
    n.infNFe.emit.enderEmit.UF.valor      = u'SP'
    n.infNFe.emit.enderEmit.CEP.valor     = u'18085520'
    #n.infNFe.emit.enderEmit.cPais.valor   = u'1058'
    #n.infNFe.emit.enderEmit.xPais.valor   = u'Brasil'
    n.infNFe.emit.enderEmit.fone.valor    = u'1534110602'
    n.infNFe.emit.IE.valor = '115944836112'

    #
    # Destinatário
    #
    n.infNFe.dest.CNPJ.valor  = '01225741000133' 
    n.infNFe.dest.xNome.valor = u'Razão Social Ltda. EPP'
    n.infNFe.dest.enderDest.xLgr.valor    = u'R. Ibiúna'
    n.infNFe.dest.enderDest.nro.valor     = u'729'
    n.infNFe.dest.enderDest.xCpl.valor    = u'sala 3'
    n.infNFe.dest.enderDest.xBairro.valor = u'Jd. Morumbi'
    n.infNFe.dest.enderDest.cMun.valor    = u'3552205'
    n.infNFe.dest.enderDest.xMun.valor    = u'Sorocaba'
    n.infNFe.dest.enderDest.UF.valor      = u'SP'
    n.infNFe.dest.enderDest.CEP.valor     = u'18085520'
    #n.infNFe.dest.enderDest.cPais.valor   = u'1058'
    #n.infNFe.dest.enderDest.xPais.valor   = u'Brasil'
    n.infNFe.dest.enderDest.fone.valor    = u'1534110602'
    n.infNFe.dest.IE.valor = u'114691048114'

    #
    # Detalhe
    #
    d1 = Det_110()
    
    d1.nItem.valor = 1
    d1.prod.cProd.valor    = u'código do produto'
    d1.prod.cEAN.valor     = u''
    d1.prod.xProd.valor    = u'Descrição do produto'
    d1.prod.NCM.valor      = u''
    d1.prod.EXTIPI.valor   = u''
    d1.prod.genero.valor   = u''
    d1.prod.CFOP.valor     = u'5101'
    d1.prod.uCom.valor     = u'UN'
    d1.prod.qCom.valor     = u'100.00'
    d1.prod.vUnCom.valor   = u'10.0000'
    d1.prod.vProd.valor    = u'1000.00'
    d1.prod.cEANTrib.valor = u''
    d1.prod.uTrib.valor    = d1.prod.uCom.valor
    d1.prod.qTrib.valor    = d1.prod.qCom.valor
    d1.prod.vUnTrib.valor  = d1.prod.vUnCom.valor
    d1.prod.vFrete.valor   = u'0.00'
    d1.prod.vSeg.valor     = u'0.00'
    d1.prod.vDesc.valor    = u'0.00'
    
    #
    # Impostos
    #
    d1.imposto.ICMS.CST.valor   = u'00'
    d1.imposto.ICMS.modBC.valor = 3
    d1.imposto.ICMS.vBC.valor   = u'1000.00'
    d1.imposto.ICMS.pICMS.valor = u'18.00'
    d1.imposto.ICMS.vICMS.valor = u'180.00'
    
    d1.imposto.IPI.CST.valor    = u'50'
    d1.imposto.IPI.vBC.valor    = u'1000.00'
    d1.imposto.IPI.pIPI.valor   = u'10.00'
    d1.imposto.IPI.vIPI.valor   = u'100.00'
    
    d1.imposto.PIS.CST.valor    = u'01'
    d1.imposto.PIS.vBC.valor    = u'1000.00'
    d1.imposto.PIS.pPIS.valor   = u'0.65'
    d1.imposto.PIS.vPIS.valor   = u'6.50'
    
    d1.imposto.COFINS.CST.valor    = u'01'
    d1.imposto.COFINS.vBC.valor    = u'1000.00'
    d1.imposto.COFINS.pCOFINS.valor   = u'3.00'
    d1.imposto.COFINS.vCOFINS.valor   = u'30.00'
    
    #
    # Os primeiros 188 caracteres desta string
    # são todos os caracteres válidos em tags da NF-e
    #
    d1.infAdProd.valor = u'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿À'

    #
    # Inclui o detalhe na NF-e
    #
    n.infNFe.det.append(d1)
    
    #
    # Totais
    #
    n.infNFe.total.ICMSTot.vBC.valor     = u'1000.00'
    n.infNFe.total.ICMSTot.vICMS.valor   = u'180.00'
    n.infNFe.total.ICMSTot.vBCST.valor   = u'0.00'
    n.infNFe.total.ICMSTot.vST.valor     = u'0.00'
    n.infNFe.total.ICMSTot.vProd.valor   = u'1000.00'
    n.infNFe.total.ICMSTot.vFrete.valor  = u'0.00'
    n.infNFe.total.ICMSTot.vSeg.valor    = u'0.00'
    n.infNFe.total.ICMSTot.vDesc.valor   = u'0.00'
    n.infNFe.total.ICMSTot.vII.valor     = u'0.00'
    n.infNFe.total.ICMSTot.vIPI.valor    = u'100.00'
    n.infNFe.total.ICMSTot.vPIS.valor    = u'6.50'
    n.infNFe.total.ICMSTot.vCOFINS.valor = u'30.00'
    n.infNFe.total.ICMSTot.vOutro.valor  = u'0.00'
    n.infNFe.total.ICMSTot.vNF.valor     = u'1100.00'
    
    #
    # O retorno de cada webservice é um dicionário
    # estruturado da seguinte maneira:
    # { TIPO_DO_WS_EXECUTADO: {
    #       u'envio'   : InstanciaDaMensagemDeEnvio,
    #       u'resposta': InstanciaDaMensagemDeResposta,
    #       }
    # }
    #
    for processo in p.processar_notas([n]):
        print
        print
        print processo.envio.xml
        print
        print processo.resposta.xml
        print
        print processo.resposta.reason
