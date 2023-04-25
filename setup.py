razze = "Dalmata", "Golden Retriever", "Labrador Retriever", "Bassotto", "Alano", "Pastore Tedesco", "Akita", "Barbone nano", "Barbone standard", "Barbone Toy", "Bobtail", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier", "Bovaro del Bernese", "Bovaro delle Fiandre", "Boxer", "Bracco Italiano", "Bull Terrier", "Bulldog", "Bulldog Francese", "Cairn Terrier", "Canaan Dog", "Cane da Montagna dei Pirenei", "Cane dei faraoni", "Carlino", "Chihuahua pelo corto", "Chihuahua pelo lungo"

database = {
'Razze cani:' : razze
}

def razza(razzadata):
    if razzadata in database['Razze cani:']:
        return razzadata
    else:
        return None
        
def tuttelerazze():
    return database['Razze cani:']