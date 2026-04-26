# Portuguese (Portugal) — derived from pt-BR with regional adjustments.
from lang import pt_br

LANG = "pt-PT"
DIR = "ltr"
LABEL = "Português (PT)"

# Map of en_string -> replacement_for_pt_pt. Anything not listed inherits from pt-BR.
_PORTUGAL_OVERRIDES = {
    "MyPetLogger — The pet journal you'll actually keep":
        "MyPetLogger — O diário do seu animal que vai mesmo manter",
    "A beautifully native iOS app for every kind of pet — dogs, cats, birds, rabbits, ferrets, and more. Medical records, walks, reminders. Private by design, no accounts, no tracking.":
        "Uma bonita aplicação iOS nativa para todo o tipo de animal — cães, gatos, aves, coelhos, furões e mais. Registos médicos, passeios, lembretes. Privada por design, sem contas, sem rastreio.",
    "A beautifully native iOS app for every moment of your pet's life. Private by design.":
        "Uma bonita aplicação iOS nativa para cada momento da vida do seu animal. Privada por design.",
    "The pet journal<br>you'll <em>actually</em> keep.":
        "O diário do seu animal<br>que vai <em>mesmo</em> manter.",
    ("MyPetLogger is the iOS app for every companion in your home — dogs, cats, birds, rabbits,\n        ferrets, hamsters and the rest. An obsessively polished place to keep every vaccine,\n        every walk, every vet visit, every milestone. It lives on your iPhone. Nowhere else.\n        No accounts. No tracking. No noise."):
        ("MyPetLogger é a aplicação iOS para todo o companheiro da sua casa — cães, gatos, aves, coelhos,\n        furões, hamsters e os restantes. Um sítio obsessivamente cuidado para guardar cada vacina,\n        cada passeio, cada visita ao veterinário, cada marco. Vive no seu iPhone. Em mais lado nenhum.\n        Sem contas. Sem rastreio. Sem ruído."),
    "See what's inside →": "Veja o que está lá dentro →",
    ("Pet apps are usually one of two things: a glorified contact list for one species, or a\n      data vacuum selling your pet's birthday to an ad broker. <strong>We wanted neither.</strong>\n      MyPetLogger is a calm, private, deeply native iOS app built around a single idea —\n      the person who loves your pet the most is you, and the place to remember their life\n      should feel like home, whether they bark, purr, chirp, or hop."):
        ("Aplicações para animais costumam ser uma de duas coisas: uma lista de contactos disfarçada para uma espécie, ou\n      um aspirador de dados que vende o aniversário do seu animal a um corretor de anúncios. <strong>Não queríamos nenhuma das duas.</strong>\n      MyPetLogger é uma aplicação iOS calma, privada e profundamente nativa construída em torno de uma única ideia —\n      a pessoa que mais ama o seu animal é você, e o sítio para recordar a vida dele\n      deve parecer-se com casa, quer ladre, ronrone, cante ou salte."),
    "Pinned pets surface first across every screen":
        "Animais fixados aparecem primeiro em todos os ecrãs",
    "Built-in camera and square cropper for portraits":
        "Câmara integrada e recorte quadrado para retratos",
    "Pet list": "Lista de animais",
    "Pet detail with medical records": "Detalhe do animal com registos médicos",
    "Português": "Português (Portugal)",
}


def _apply(pairs):
    out = []
    for en, pt in pairs:
        if en in _PORTUGAL_OVERRIDES:
            out.append((en, _PORTUGAL_OVERRIDES[en]))
        else:
            out.append((en, pt))
    return out


HOME = _apply(pt_br.HOME)
PRIVACY = _apply(pt_br.PRIVACY)
TERMS = _apply(pt_br.TERMS)
AGE = _apply(pt_br.AGE)
