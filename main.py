from flet import *
import random
import time

def main (page:Page):
    page.title= ("eslam elmasry")
    page.window.width =390
    page.window.height =740
    page.window.top = 0
    page.window.left = 960
    page.padding =0
    #################################
    imo= ['thems/lo1.jpg','thems/lo3.jpg','thems/lo4.jpg','thems/lo5.jpg']
    imges= random.sample(imo,3)
    for x in imges :
        im = Image (src=f'{x}',
                     width=390,
                     opacity=0.9,
                       height=740 ,
                         top=0 , 
                         fit=ImageFit.FILL)

    #################################
    mytime= time.strftime("%H:%M")
    #################################
    colors = ['green','blue','purple' ]
    finel = random.sample(colors,2)
    for b in finel:
        timo = Text(mytime, size=53, color=f'{b}', font_family='Impact')


    page.add(
        Container(
            Stack([
                im,
                
                Container(
                    Column([
                        Column(
                            spacing=10,
                            height=740,
                            width=390,
                            scroll= ScrollMode.HIDDEN,
                            controls=[
                                Row([
                                    Text("\n\n\n welcome", size=43 , font_family='Sitka Small' , color='white' , weight='bold')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    timo
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text("تطبيق خدمات برمجية\n\n\n\n\n\n", size=23 , font_family='IBM Plex Sans Arbice' , color='white' , weight='bold')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    ElevatedButton(
                                        "الدخول الى لوحة التحكم",
                                        width=270,
                                        style=ButtonStyle(bgcolor='amber', color='black', padding=18)

                                    )
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    ElevatedButton(
                                        "انشاء حساب جديد",
                                        width=270,
                                        style=ButtonStyle(bgcolor='amber', color='black', padding=18)

                                    )
                                ],alignment=MainAxisAlignment.CENTER),

                            ]
                            )

                    ])
                    
                )
            ])
        )
    )




    page.update()


app(main)
