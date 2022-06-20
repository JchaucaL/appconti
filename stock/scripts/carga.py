from dbfread import DBF
import pandas as pd
from datetime import datetime




def run():
    from stock.models import Item , Escalas 
    from django.contrib.auth.models import User
    dbf = DBF('C:/XPROW/DBF/T180-10.dbf', encoding='latin1')
    frame = pd.DataFrame(iter(dbf))
    filtered_df = frame.query('STOCK > 1')
    print(filtered_df)
    Item.objects.all().delete()
    Escalas.objects.all().delete()
    usuario = User.objects.get(username='jchauca')

    for row in filtered_df.index:
        Codigo = filtered_df['CODIGO'][row]
        Descrip = filtered_df['DESCRIP'][row]

        cDescrip = '%s %s'%(Codigo, Descrip)
        print(cDescrip)
        item = Item(Codigo= filtered_df['CODIGO'][row],
                        name=cDescrip,
                        quantity=filtered_df['STOCK'][row],
                        status = 'PENDING',
                        user = usuario  ,
                        date = datetime.now(),
                        updated_at = datetime.now(),
                        created_at = datetime.now(),
                        )
        item.save()

    for row in frame.index:
        print(frame['CODIGO'][row],frame['CANTIDAD'][row])
        cDescto="{:.2%}".format(frame['DESCTO'][row])
        escalas = Escalas(Codigo=frame['CODIGO'][row],
                       Unidad=frame['UNIDAD'][row],
                       Descrip=frame['DESCRIP'][row],
                       Cantidad=frame['CANTIDAD'][row],
                       Descto=cDescto,
                       Valor_Vta=frame['VALOR_VTA'][row],
                       Prec_Fin=frame['PREC_FIN'][row],
                       Stock=frame['STOCK'][row],
                       )
        escalas.save()