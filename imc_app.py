import flet as ft

def main(page: ft.Page):

    def calcular(e):
        if not peso.value:
            peso.error_text = 'Peso não pode ficar vazio'
            page.update()
        if not altura.value:
            altura.error_text = 'Altura não pode ficar vazio'
            page.update()
        else:
            peso.value = float(peso.value.replace(',','.'))
            altura.value = float(altura.value.replace(',','.'))
            imc = peso.value/(altura.value**2)
            imc_result.value = f'Valor do IMC: {imc:,.2f}.'
            if imc < 16.9:
                imc_msg.value = 'Possível anorexia. Procure um médico.'
            elif imc < 18.5:
                imc_msg.value = 'Você está abaixo do peso.'
            elif imc < 25:
                imc_msg.value = 'Você está no seu peso ideal.'
            elif imc < 30:
                imc_msg.value = 'Você está acima do peso.'
            elif imc < 35:
                imc_msg.value = 'Você está obeso.'
            elif imc < 40:
                imc_msg.value = 'Você está com obesidade nível II.'
            else:
                imc_msg.value = 'Você está com obeisdade mórbida.'

            peso.value = ''
            altura.value = ''

            page.update()

    page.title = 'IMC - Índice de Massa Corporal'
    page.scroll = 'adaptive'

    peso = ft.TextField(label='Peso', suffix_text='kg', autofocus=True)
    altura = ft.TextField(label='Altura', suffix_text='m')
    imc_result = ft.Text(size=35)
    imc_msg = ft.Text(size=30)

    page.add(
        ft.Text('IMC - Índice de Massa Corporal', size=40, weight=ft.FontWeight.BOLD),
        peso,
        altura,
        ft.TextButton('Calcular IMC', on_click=calcular),
        imc_result,
        imc_msg
    )

    page.update()

ft.app(main)