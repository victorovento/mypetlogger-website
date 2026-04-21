# British English variant. Small delta from en-US source.
LANG = "en-GB"
DIR = "ltr"
LABEL = "English (UK)"

# Only strings that actually differ between US and UK English.
# Keep USD pricing labels — Apple App Store presents per-region pricing automatically.

_DELTAS = [
    # Spelling
    ("beautifully organized", "beautifully organised"),
    ("colors, markings", "colours, markings"),
    ("species-specific colors", "species-specific colours"),
    ("color palette", "colour palette"),
    ("Our favorite option", "Our favourite option"),
    ("favorite", "favourite"),
    ("organize", "organise"),
    ("recognize", "recognise"),
    ("realize", "realise"),
    ("personalized", "personalised"),
    ("non-personalized", "non-personalised"),
    ("centered", "centred"),
    ("anonymous", "anonymous"),  # same
    ("behavior", "behaviour"),
    ("minimize", "minimise"),
    ("optimize", "optimise"),
    ("license", "licence"),  # noun usage in legal pages
    ("traveled", "travelled"),
    ("canceled", "cancelled"),
    ("cancelled", "cancelled"),  # already correct
    ("United States limited liability company", "United States limited liability company"),
    ("zip codes", "post codes"),
    ("cell phones", "mobile phones"),
    # Punctuation: en-US uses straight quotes everywhere — leave as is
    # Date format: keep ISO-style "April 20, 2026" → "20 April 2026" in legal pages
    ("Last updated: April 20, 2026", "Last updated: 20 April 2026"),
    # Footer language link label
]

HOME = list(_DELTAS) + [
    # Eyebrow + quote tweaks
    ("\"Hey Siri, start a walk in MyPetLogger\"",
     "\"Hey Siri, start a walk in MyPetLogger\""),  # identical
]

PRIVACY = list(_DELTAS)
TERMS = list(_DELTAS)
AGE = list(_DELTAS)
