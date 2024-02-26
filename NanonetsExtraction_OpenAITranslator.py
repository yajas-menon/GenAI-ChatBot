import requests
import sys
import json
import os
import openai

url = 'https://app.nanonets.com/api/v2/OCR/Model/1a1ba242-6a57-4095-b9b2-4e36be81a74b/LabelFile/?async=false'

data = {'file': open(r'C:\Users\potta.nikhil\Downloads\test file.png', 'rb')}
# data = {'file': open(sys.argv[1], 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('GXzBEKcARRutCFgxBGLZ8WAUD9XhLFbz', ''), files=data)
# response = {'message': 'Success', 'result': [{'message': 'Success', 'input': 'test file.png', 'prediction': [{'id': 'acf933be-d289-4029-b7f6-d9caa0221010', 'label': 'Address', 'xmin': 335, 'ymin': 53, 'xmax': 1665, 'ymax': 311, 'score': 0, 'ocr_text': 'ALMACONTACT S.A.S \nEntidad Contratante : Avenida Carrera . 15 # 110-45 P 6 \nBogotá , D.C. , Colombia \nsiguiente ( s ) pagina', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': 'c81df03a-4cf4-4afd-9618-f70884cd54fc'}, {'id': '0eb1b8ea-ccbc-4f8e-bc18-45f59379db36', 'label': 'Certification_details', 'xmin': 232, 'ymin': 3916, 'xmax': 1828, 'ymax': 4514, 'score': 0, 'ocr_text': 'Carolina Prieto Carranza \nGerente Técnico BUREAU VERITAS \nCertification Certificado No. CO23.06187 Versión : No. 1 Fecha de Revisión : 08 mayo 2023 \nLa validez de este certificado depende de la validez del certificado principal , que expira \n31 octubre 2025 S \n4 VER RITAS \n1828 O ONAC \nACREDITADO \nISO / IEC 17021-1 : \n10 - CSG - 007', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': '0ced553b-084d-4d8f-a8d5-09f51fc82929'}, {'id': '50fe7044-68e8-4d87-a681-8fae21e9066b', 'label': 'Standard', 'xmin': 52, 'ymin': 362, 'xmax': 1793, 'ymax': 536, 'score': 0, 'ocr_text': 'BVQI Colombia Ltda . certifica que el Sistema de Gestión de la organización ha sido \nauditado y se ha encontrado conforme con los requerimientos de las normas de \nSistema de Gestión que se detallan a continuación', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': '370aa5bc-141a-42f9-8304-82ee0a87dfe9'}, {'id': '986340ab-5b5d-461e-8da8-f6dbb9075946', 'label': 'Certification_Cycle', 'xmin': 94, 'ymin': 1253, 'xmax': 1884, 'ymax': 1604, 'score': 0, 'ocr_text': 'Fecha de Inicio del Ciclo Original de Certificación : Fecha de Vencimiento del ciclo previo : Fecha de Auditoria de Certificación : \nFecha de Inicio del ciclo de Certificación : 08 mayo 2023 \nN / A \n27 febrero 2023 \n08 mayo 2023 Sujeto a la operación continua y satisfactoria del Sistema de Gestión de la organización , este certificado vence el : 31 octubre 2025 T', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': '397b6402-4e54-4460-b08f-bbbe17be0941'}, {'id': '91519a93-2c05-47fa-a64d-3c0a8bcbf4fa', 'label': 'Declaration', 'xmin': 45, 'ymin': 870, 'xmax': 1811, 'ymax': 1183, 'score': 0, 'ocr_text': 'PRESTACIÓN DE SERVICIOS DE CONTACT CENTER Y PROCESOS ASOCIADOS A LA \nEXTERNALIZACIÓN DE SERVICIOS BPO PARA CLIENTES NACIONALES E \nINTERNACIONALES . \nDeclaración de aplicabilidad : Del 10/02/2023 . Exclusión de controles A.6.2.2 - A.14.2.7 5', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': '52fc6dbd-4afa-45c4-b17e-fa62e94c81ed'}, {'id': '4fc0ea0b-1849-438c-9b9c-80927b8f4156', 'label': 'Certification_Scope', 'xmin': 0, 'ymin': 0, 'xmax': 0, 'ymax': 0, 'score': 0, 'ocr_text': 'Nombre del \nSitio \nH.O \nSITIO 1 \nSITIO 2 Dirección del Sitio \nAvenida Carrera . 15 # 110-45 \nP 6 Basik \nBogotá D.C. , Colombia \nCalle 162 # 21-91 Toberín \nBogotá D.C. , Colombia \nCarrera , 48A # 61Sur - 75 \nSabaneta , Antioquía , Colombia I Alcance del Sitio \nPRESTACIÓN DE SERVICIOS DE \nCONTACT CENTER Y PROCESOS \nASOCIADOS A LA EXTERNALIZACIÓN DE \nSERVICIOS BPO PARA CLIENTES \nNACIONALES E INTERNACIONALES . \nPRESTACIÓN DE SERVICIOS DE \nCONTACT CENTER Y PROCESOS \nASOCIADOS A LA EXTERNALIZACIÓN DE \nSERVICIOS BPO PARA CLIENTES \nNACIONALES E INTERNACIONALES . \nPRESTACIÓN DE SERVICIOS DE \nCONTACT CENTER Y PROCESOS \nASOCIADOS A LA EXTERNALIZACIÓN DE \nSERVICIOS BPO PARA CLIENTES \nNACIONALES E INTERNACIONALES .', 'type': 'field', 'status': 'correctly_predicted', 'page_no': 0, 'label_id': 'bf035ce8-321d-4793-b0a2-c44cf7e8e123'}], 'page': 0, 'request_file_id': 'f38e951c-24df-481d-8f91-0524a68ccd85', 'filepath': 'uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg', 'id': '3a9242b5-aeb5-11ee-953b-a61bf39d42a9', 'rotation': 0, 'file_url': 'uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/RawPredictions/f38e951c-24df-481d-8f91-0524a68ccd85.png', 'request_metadata': '', 'processing_type': 'sync', 'size': {'width': 1991, 'height': 4721}, 'raw_ocr_api_response': {'results': None}}], 'signed_urls': {'uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg': {'original': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?expires=1704794795&or=0&s=817657bedf52e86e32aa8e4e02bec0b1', 'original_compressed': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?auto=compress&expires=1704794795&or=0&s=07060d17039cfdd8b59c6224228c2817', 'thumbnail': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?auto=compress&expires=1704794795&w=240&s=f03b81c7931a5734b873bab0bb334c28', 'acw_rotate_90': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?auto=compress&expires=1704794795&or=270&s=1b4c26408330870ba5336b6822d8f295', 'acw_rotate_180': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?auto=compress&expires=1704794795&or=180&s=edb07ce0c31db43cc20387130cade554', 'acw_rotate_270': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?auto=compress&expires=1704794795&or=90&s=b2dad93b5023938a3dcfabcb67a7e848', 'original_with_long_expiry': 'https://nnts.imgix.net/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/PredictionImages/348c0345-5a25-4a86-8195-c5bb9faaffda.jpeg?expires=1720332395&or=0&s=f772392bf7d6e31eded8b145250fc080'}, 'uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/RawPredictions/f38e951c-24df-481d-8f91-0524a68ccd85.png': {'original': 'https://nanonets.s3.us-west-2.amazonaws.com/uploadedfiles/1a1ba242-6a57-4095-b9b2-4e36be81a74b/RawPredictions/f38e951c-24df-481d-8f91-0524a68ccd85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA5F4WPNNTLX3QHN4W%2F20240109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240109T060635Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&response-cache-control=no-cache&X-Amz-Signature=0492c5822ef69d0fb38a20675d0ca4d5e5b88422c4c42140bd5a239765b5f3f8', 'original_compressed': '', 'thumbnail': '', 'acw_rotate_90': '', 'acw_rotate_180': '', 'acw_rotate_270': '', 'original_with_long_expiry': ''}}}
response = response.json()
data = response['result'][0]['prediction']
Response_dict = {}
translate_output_dict ={}
for item in data:
    Response_dict[item['label']] = item['ocr_text']

print(Response_dict)

for each_label in Response_dict:

    openai.api_type = "azure"
    openai.api_base = "https://rglegal2.openai.azure.com/"
    openai.api_version = "2023-07-01-preview"
    openai.api_key = "cf1a2de59c334e82bc44f25b80864009"

    message_text = [{"role": "system",
                     "content": "translate it to english - " +Response_dict[each_label]}]
    completion = openai.ChatCompletion.create(
        engine="LegalTest",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    translate_output_dict[each_label] = completion['choices'][0]['message']['content']

print(translate_output_dict)