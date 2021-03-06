# -*- coding: utf-8 -*-


db.define_table('ficha_pre_natal_evolucao',
                Field('id_ficha', 'reference ficha_clinica_pre_natal',
                      writable=False, readable=False),
                Field('consulta_numero', requires=IS_NOT_EMPTY()),
                # Evolução gravidez
                Field('data_EG', label='Data'),
                Field('ig_EG', label='IG(semanas)'),
                Field('peso_EG', label='Peso(kg)'),
                Field('pa_EG', label='PA max/min (mmHg)'),
                Field('altura_uterina_EG', label='Altura uterina (cm)'),
                Field('apresentacao_fetal_EG', label='Apresentação fetal'),
                Field('movimentos_fetais_EG', label='Movimentos fetais'),
                Field('bcf_EG', label='BCF'),
                Field('edema_EG', label='Edema MMII'),
                # Exames laboratoriais
                Field('data_EL'),
                Field('tipo_sanguineo_EL', label='Tipo Sanguineo'),
                Field('hbht_EL', label='Hb / Ht'),
                Field('glicenia_jejum_EL', label='Glicenia jejum'),
                Field('totg_EL', label='TOTG 50g'),
                Field('vdrl_EL', label='VDRL'),
                Field('hbsag_EL', label='HbsAg'),
                Field('hiv_EL', label='HIV'),
                Field('toxoplasmose_EL', label='Toxoplasmose'),
                Field('rubeola_EL', label='Rubéola'),
                Field('urinal_EL', label='Urinal'),
                Field('urocultura_EL', label='Urocultura'),
                Field('papanicolaou_EL', label='Papanicolaou'),
                Field('outros_EL', label='Outros'),
                # Ultra-Sonografia
                Field('data_US', label='Data'),
                Field('ig_dum_US', label='IG DUM'),
                Field('ig_usg_US', label='IG USG'),
                Field('peso_fetal_US', label='Peso fetal'),
                Field('placenta_US', label='Placenta'),
                Field('liquido', label='Líquido'),
                Field('outros_US', label='Outros'),
                Field('observacoes_US', label='Observações'),
                # Intercorrências/Conduta
                Field('data_IC'),
                Field('ic_IC', label='Intercorrências/Conduta'),
                )
