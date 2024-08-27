from fasthtml.common import Title, Header, Main, Footer, Nav, Ul, A, Li, H1, H2, H3, H4, H6, Section, I, fast_app, Link, Hgroup, P, Img, Grid, Div, Strong
from app.view.articles import left_text_article, right_text_article, left_text_article_with_accordion

app, route = fast_app(
	hdrs=(
		Link(
			rel="stylesheet",
			href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.colors.min.css",
		),
		# To add icons
		Link(
			rel="stylesheet",
			href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
		),
		Link(
			rel="stylesheet",
			href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pink.min.css",
		),
		Link(
			rel="stylesheet",
			href="app/assets/css/main.css",
		),
	),
	live=True,
)


def footer() -> Footer:
	return Footer(
		Nav(
			Ul(
				Li("left"),
			),
			Ul(
				Li("center 1"),
				Li("center 2"),
			),
			Ul(
				Li("right"),
			),
			cls="container",
		),
		cls="container-fluid pico-background-slate-900",
	)


def header() -> Header:
	return Header(
		Nav(
			Ul(
				A(
					Li(
						Strong("Projetos"),
					),
					href="#",
				),
				A(
					Li(
						Strong("Serviços"),
					),
					href="#",
				),
				A(
					Li(
						Strong("Contato"),
					),
					href="#",
				),
			),
			Ul(
				A(
					Li(I(cls="fa-brands fa-instagram")),
					href="#",
				),
				A(
					Li(I(cls="fa-solid fa-envelope")),
					href="#",
				),
			),
			cls="container",
		),
		cls="pico-background-slate-900",
	)


@route("/")
async def get():  # noqa: ANN201
	return (
		Title("Cascales"),
		header(),
		Main(
			Section(
				Nav(
					Ul(
						Li(
							A(
								Img(src="app/assets/img/logo-1.jpeg", alt="logo", cls="logo-img"),
								href="/",
							),
						),
						Li(
							Hgroup(
								H1("Cascales"),
								P("Engenharia & Arquitetura"),
							),
						),
					),
				),
				cls="grid-centered",
			),
			Section(
				left_text_article(
					"Algum titulo qualquer",
					"Algum texto qualquer " * 20,
					"https://25.media.tumblr.com/tumblr_krvv9ssJAe1qa9hjso1_1280.jpg",
				),
			),
			Section(
				right_text_article(
					"Algum titulo qualquer",
					"Algum texto qualquer " * 5,
					"https://cdn2.thecatapi.com/images/2de.jpg",
				),
			),
			Section(
				left_text_article_with_accordion(
					"Algum titulo qualquer",
					"Algum texto qualquer " * 10,
					"https://cdn2.thecatapi.com/images/484.jpg",
					"Mais 4 fotos, mas é flexível",
					"https://cdn2.thecatapi.com/images/MjA3NzYxNQ.jpg",
					"https://cdn2.thecatapi.com/images/H_UWbOfra.jpg",
					"https://cdn2.thecatapi.com/images/bdd.jpg",
					"https://cdn2.thecatapi.com/images/957.jpg",
				),
			),
			cls="container",
		),
		footer(),
	)
