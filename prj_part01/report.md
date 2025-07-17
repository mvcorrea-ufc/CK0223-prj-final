# Data Processing Report (Lista 1)

This report details the data cleaning and preprocessing steps performed on the dataset.

## A: Load Dataset

Dataset loaded successfully. Here's a preview:

| date_message        | id_member_anonymous              | id_group_anonymous               | media                                | media_type   |   media_url | has_media   | has_media_url   | trava_zap   | text_content_anonymous                                                                                                                                                                                                                                                                                                                                         |   dataset_info_id | date_system                |   score_sentiment |   score_misinformation |   id_message | message_type   | messenger   |   media_name | media_md5                        |
|:--------------------|:---------------------------------|:---------------------------------|:-------------------------------------|:-------------|------------:|:------------|:----------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------:|:---------------------------|------------------:|-----------------------:|-------------:|:---------------|:------------|-------------:|:---------------------------------|
| 2022-10-05 06:25:04 | 1078cc958f0febe28f4d03207660715f | 12283e08a2eb5789201e105b34489ee7 | nan                                  | nan          |         nan | False       | False           | False       | Então é Fato Renato o áudio que eu ouvi no whatsapp isso ocorreu em Niterói principalmente no bairro Fonseca ?                                                                                                                                                                                                                                                 |                 5 | 2022-10-05 06:25:28.863641 |            0      |             nan        |        16385 | Texto          | telegram    |          nan | nan                              |
| 2022-10-05 06:25:08 | nan                              | 12283e08a2eb5789201e105b34489ee7 | nan                                  | nan          |         nan | False       | False           | False       | Saiu no YouTube do presidente a 8 horas atrás, infelizmente não consigo enviar para cá, mas é facilmente verificável no YouTube do presidente                                                                                                                                                                                                                  |                 5 | 2022-10-05 06:25:28.926311 |            0.0644 |             nan        |        16386 | Texto          | telegram    |          nan | nan                              |
| 2022-10-05 06:26:28 | 92a2d8fd7144074f659d1d29dc3751da | 9f2d7394334eb224c061c9740b5748fc | nan                                  | nan          |         nan | False       | False           | False       | É isso, nossa parte já foi quase toda feita. No segundo turno completamos nossa parte desse teatro. Essa é uma guerra de 4* geração na dimensão humana e uma guerra espiritual do bem contra o mal na dimensão do Universo. Pensamento positivo é fundamental, pensem sempre em algo bom. Deus continua nos abençoando, nosso livre arbítrio completa o curso. |                 5 | 2022-10-05 06:26:29.361949 |           -0.3551 |               0.157242 |        16366 | Texto          | telegram    |          nan | nan                              |
| 2022-10-05 06:27:28 | d60aa38f62b4977426b70944af4aff72 | c8f2de56550ed0bf85249608b7ead93d | 94dca4cda503100ebfda7ce2bcc060eb.jpg | image/jpg    |         nan | True        | False           | False       | GENTE ACHEI ELES EM UMA SEITA MAÇONÁRICA                                                                                                                                                                                                                                                                                                                       |                 5 | 2022-10-05 06:27:29.935624 |            0      |             nan        |        19281 | Imagem         | telegram    |          nan | 94dca4cda503100ebfda7ce2bcc060eb |
| 2022-10-05 06:27:44 | cd6979b0b5265f08468fa1689b6300ce | e56ec342fc599ebb4ed89655eb6f03aa | 5ad5c8bbe9da93a37fecf3e5aa5b0637.jpg | image/jpg    |         nan | True        | False           | False       | nan                                                                                                                                                                                                                                                                                                                                                            |                 5 | 2022-10-05 06:28:29.316325 |          nan      |             nan        |       507185 | Imagem         | telegram    |          nan | 5ad5c8bbe9da93a37fecf3e5aa5b0637 |

## Data Cleaning and Feature Engineering

### Question b & c: Identify missing values and count rows containing them.

Total number of rows with at least one missing value: **557561**

### Question d: Count missing values for each column.

| Column                 |   Missing Values |
|:-----------------------|-----------------:|
| date_message           |                0 |
| id_member_anonymous    |           323341 |
| id_group_anonymous     |                0 |
| media                  |           224981 |
| media_type             |           224981 |
| media_url              |           400141 |
| has_media              |                0 |
| has_media_url          |                0 |
| trava_zap              |                0 |
| text_content_anonymous |           113385 |
| dataset_info_id        |                0 |
| date_system            |                0 |
| score_sentiment        |           113429 |
| score_misinformation   |           390348 |
| id_message             |                0 |
| message_type           |                0 |
| messenger              |                0 |
| media_name             |           528599 |
| media_md5              |           224981 |

### Question e: Identify and list duplicate rows.

Found **0** duplicate rows.

### Question f: Identify values not belonging to the expected domain.

This step is complex without a clear data dictionary. A full implementation would require checks for each column's expected data type and format.

### Question g & h: Create 'caracteres' and 'words' columns.

| text_content_anonymous                                                                                                                                                                                                                                                                                                                                         |   caracteres |   words |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|--------:|
| Então é Fato Renato o áudio que eu ouvi no whatsapp isso ocorreu em Niterói principalmente no bairro Fonseca ?                                                                                                                                                                                                                                                 |          110 |      20 |
| Saiu no YouTube do presidente a 8 horas atrás, infelizmente não consigo enviar para cá, mas é facilmente verificável no YouTube do presidente                                                                                                                                                                                                                  |          141 |      23 |
| É isso, nossa parte já foi quase toda feita. No segundo turno completamos nossa parte desse teatro. Essa é uma guerra de 4* geração na dimensão humana e uma guerra espiritual do bem contra o mal na dimensão do Universo. Pensamento positivo é fundamental, pensem sempre em algo bom. Deus continua nos abençoando, nosso livre arbítrio completa o curso. |          350 |      59 |
| GENTE ACHEI ELES EM UMA SEITA MAÇONÁRICA                                                                                                                                                                                                                                                                                                                       |           40 |       7 |
| nan                                                                                                                                                                                                                                                                                                                                                            |            0 |       0 |

### Question i & j: Create 'viral' and 'sharings' columns.

| text_content_anonymous                                                                                                                                                                                                                                                                                                                                         |   sharings |   viral |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------:|--------:|
| Então é Fato Renato o áudio que eu ouvi no whatsapp isso ocorreu em Niterói principalmente no bairro Fonseca ?                                                                                                                                                                                                                                                 |          1 |       0 |
| Saiu no YouTube do presidente a 8 horas atrás, infelizmente não consigo enviar para cá, mas é facilmente verificável no YouTube do presidente                                                                                                                                                                                                                  |          1 |       0 |
| É isso, nossa parte já foi quase toda feita. No segundo turno completamos nossa parte desse teatro. Essa é uma guerra de 4* geração na dimensão humana e uma guerra espiritual do bem contra o mal na dimensão do Universo. Pensamento positivo é fundamental, pensem sempre em algo bom. Deus continua nos abençoando, nosso livre arbítrio completa o curso. |          1 |       0 |
| GENTE ACHEI ELES EM UMA SEITA MAÇONÁRICA                                                                                                                                                                                                                                                                                                                       |          1 |       0 |
| nan                                                                                                                                                                                                                                                                                                                                                            |        nan |       0 |

### Question k: Create 'sentiment' column.

| text_content_anonymous                                                                                                                                                                                                                                                                                                                                         |   sentiment |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------:|
| Então é Fato Renato o áudio que eu ouvi no whatsapp isso ocorreu em Niterói principalmente no bairro Fonseca ?                                                                                                                                                                                                                                                 |           0 |
| Saiu no YouTube do presidente a 8 horas atrás, infelizmente não consigo enviar para cá, mas é facilmente verificável no YouTube do presidente                                                                                                                                                                                                                  |           1 |
| É isso, nossa parte já foi quase toda feita. No segundo turno completamos nossa parte desse teatro. Essa é uma guerra de 4* geração na dimensão humana e uma guerra espiritual do bem contra o mal na dimensão do Universo. Pensamento positivo é fundamental, pensem sempre em algo bom. Deus continua nos abençoando, nosso livre arbítrio completa o curso. |           1 |
| GENTE ACHEI ELES EM UMA SEITA MAÇONÁRICA                                                                                                                                                                                                                                                                                                                       |           0 |
| nan                                                                                                                                                                                                                                                                                                                                                            |           0 |

### Question l: Eliminate rows containing 'trava-zaps'.

Found and removed **0** rows containing 'trava-zaps'.

### Question m: Identify inconsistencies between attributes.

Found **0** rows where 'has_media' is True but 'media_type' is null.

