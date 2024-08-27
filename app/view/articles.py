from fasthtml.common import Nav, Ul, Li, H4, H5, H6, P, Article, Img, Header, Details, Summary, Grid, Div, Strong


def left_text_article(header: str, paragraph: str, img_src: str) -> Article:
	return Article(
		Grid(
			Div(
				H4(header),
				P(paragraph),
			),
			Div(
				Img(src=img_src),
			),
		),
	)


def right_text_article(header: str, paragraph: str, img_src: str) -> Article:
	return Article(
		Grid(
			Div(
				Img(src=img_src),
			),
			Div(
				H4(header),
				P(paragraph),
			),
		),
	)


def left_text_article_with_accordion(
	header: str,
	paragraph: str,
	img_src: str,
	accordion_summary: str,
	img_src_1: str,
	img_src_2: str,
	img_src_3: str,
	img_src_4: str,
) -> Article:
	return Article(
		Header(
			Grid(
				Div(
					H4(header),
					P(paragraph),
				),
				Div(
					Img(src=img_src),
				),
			),
		),
		Details(
			Summary(Strong(accordion_summary)),
			Grid(
				Div(
					Img(src=img_src_1),
				),
				Div(
					Img(src=img_src_2),
				),
				Div(
					Img(src=img_src_3),
				),
				Div(
					Img(src=img_src_4),
				),
			),
		),
	)
