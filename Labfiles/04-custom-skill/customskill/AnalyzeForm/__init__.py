from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Replace these values with your actual endpoint and key
endpoint = "https://modelprebuilt.cognitiveservices.azure.com/"
key = "7a72e8376d2e4784923978d9d7908736"
model_id = "CVFormsModel"  # Replace with your custom model ID

# Replace this with the URL of the document you want to analyze
form_url = "https://practicecustom.blob.core.windows.net/testdoc/testform.pdf"

# Initialize the Form Recognizer client
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Analyze the document
poller = document_analysis_client.begin_analyze_document_from_url(model_id, form_url)
result = poller.result()

# Process the analysis results
for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    for name, field in document.fields.items():
        print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field.value, field.confidence))

# Add additional processing based on your application needs

