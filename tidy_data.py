import pandas as pd

df = pd.read_csv("nedlasting.csv", delimiter=";")

# Drop unnecessary columns
df = df.drop(
    ["Skoletype", "Vurderingsområde", "Eierform", "Måleenhet"], axis=1
).reset_index()
# Tidy column names
df = df.rename(
    columns={
        "Enhetsnavn": "enhetsnavn",
        "Statistikk": "statistikk",
        "Indikator/delskår": "indikator_delskar",
        "Periode": "periode",
        "Trinn": "trinn",
        "Kjønn": "kjonn",
        "Verdi": "verdi",
    }
)

# Replace missing values
df = df.replace(".", "")

# Write modified dataframe to file
df.to_csv("results.csv", index=False)
