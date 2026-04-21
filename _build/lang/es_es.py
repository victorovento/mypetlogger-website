# Spanish (Castilian / Spain) — derived from es-LA with regional adjustments.
from lang import es_la

LANG = "es-ES"
DIR = "ltr"
LABEL = "Español (España)"

# Replace selected es-LA translations with their Spain-specific variants.
# Map of (en_string, replacement_for_es_es). Anything not listed inherits from es-LA.
_SPAIN_OVERRIDES = {
    # Greetings, second-person plural cues
    "Open the app and start. No email, no password, no onboarding maze.":
        "Abre la app y empieza. Sin correo electrónico, sin contraseña, sin laberinto de bienvenida.",
    "Open the app and start. No email, no password, no onboarding maze. If you turn on iCloud sync, your records move between your own devices through your own Apple ID — never through us.":
        "Abre la app y empieza. Sin correo electrónico, sin contraseña, sin laberinto de bienvenida.",

    # Vocab differences
    "kibble": "pienso",
    "carrete": "carrete",  # same in Spain
    # "Mira qué tiene dentro" → Spain "Mira lo que hay dentro"
    "See what's inside →": "Mira lo que hay dentro →",
    # Latam often uses "verdadero" / Spain prefers same
    # Pricing / labels
    "Free": "Gratis",
    "Lifetime": "De por vida",
    "Pay once. Yours forever. Our favorite option.":
        "Paga una vez. Tuya para siempre. Nuestra opción favorita.",
    # Footer language label
    # Founder note: "tres años queriendo organizar" → Spain "tres años con la intención de organizar"
    ("I had been meaning to organize my dogs' vaccination cards for about three years.\n"
     "        The paperwork lived in a folder on my desk, a second folder in a drawer, a Google Drive\n"
     "        with conflicting filenames, three notes on my phone, and my memory — which was\n"
     "        the least reliable archive of the five. Every time I went to the vet, I re-discovered\n"
     "        the same facts, printed the same printouts, and re-wrote the same dates on the same\n"
     "        forms."):
        ("Llevaba unos tres años con la intención de organizar las cartillas de vacunación de mis perros.\n"
         "        El papeleo vivía en una carpeta sobre mi escritorio, una segunda carpeta en un cajón, un Google Drive\n"
         "        con nombres de archivo en conflicto, tres notas en mi móvil, y mi memoria — que era\n"
         "        el archivo menos fiable de los cinco. Cada vez que iba al veterinario, redescubría\n"
         "        los mismos datos, imprimía los mismos folios y volvía a escribir las mismas fechas en los mismos\n"
         "        formularios."),
    ("The apps I found either wanted me to make an account, or wanted to show me ads for\n"
     "        kibble, or wanted to sell me a subscription for a feature that should have been\n"
     "        basic. None of them felt like the kind of thing you'd open on a quiet Sunday and\n"
     "        be glad to sit with for ten minutes."):
        ("Las apps que encontré o querían que me crease una cuenta, o me querían enseñar anuncios de\n"
         "        pienso, o me querían vender una suscripción por una función que debería haber sido\n"
         "        básica. Ninguna parecía ese tipo de app que abrirías un domingo tranquilo y\n"
         "        que disfrutarías usar diez minutos."),
    "Hey Siri, start a walk in MyPetLogger": "Oye Siri, empieza un paseo en MyPetLogger",
    "\"Hey Siri, start a walk in MyPetLogger\"": "\"Oye Siri, empieza un paseo en MyPetLogger\"",
    # Common verb: "elige" works in Spain too, keep
}


def _apply(pairs):
    out = []
    for en, es in pairs:
        if en in _SPAIN_OVERRIDES:
            out.append((en, _SPAIN_OVERRIDES[en]))
        else:
            out.append((en, es))
    return out


HOME = _apply(es_la.HOME)
PRIVACY = _apply(es_la.PRIVACY)
TERMS = _apply(es_la.TERMS)
AGE = _apply(es_la.AGE)
