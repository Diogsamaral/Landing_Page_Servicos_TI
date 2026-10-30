import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Lead

@csrf_exempt
def capture_lead(request):
    # Trata a submissão do formulário
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            lead = Lead.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                company=data.get('company'),
                phone=data.get('phone'),
                service_interest=data.get('service_interest'),
                message=data.get('message')
            )

            # Envio de e-mail de notificação
            receiver_email = os.getenv('EMAIL_RECEIVER', 'seu-email@empresa.com')
            subject = f"🚀 Novo Lead Capturado: {lead.name}"
            email_content = f"""
            Novo contato recebido na Landing Page!

            • Nome: {lead.name}
            • E-mail: {lead.email}
            • Empresa: {lead.company or 'Não informado'}
            • Telefone: {lead.phone or 'Não informado'}
            • Serviço de Interesse: {lead.service_interest or 'Geral'}
            • Mensagem: {lead.message or 'Nenhuma mensagem'}
            • Data: {lead.created_at.strftime('%d/%m/%Y %H:%M')}
            """

            send_mail(
                subject=subject,
                message=email_content,
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[receiver_email],
                fail_silently=True,
            )

            return JsonResponse({'status': 'success', 'message': 'Lead cadastrado com sucesso!'}, status=201)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # Caso acesse via GET diretamente no navegador
    elif request.method == 'GET':
        return JsonResponse({'status': 'info', 'message': 'Endpoint ativo. Envie uma requisição POST com os dados do formulário.'})

    return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)