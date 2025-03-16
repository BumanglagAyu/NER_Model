Dataset of the World Digital Library

https://lccn.loc.gov/2020446966

ABOUT THIS DATASET:

This dataset collects the metadata for all items from the World Digital Library (WDL) project in seven languages.

WDL presented 19,147 items contributed by partner organizations worldwide as well as content from Library of Congress collections. The original WDL website and descriptive metadata were translated from the original English records and made available in six additional languages: Spanish, Portuguese, French, Arabic, Russian, and Chinese. All item records include narrative descriptions submitted by the contributing partners and enhanced by WDL researchers to contextualize the item and its cultural and historical importance.

For additional context on the WDL collections, see https://www.loc.gov/collections/world-digital-library/about-this-collection/

For additional information and contact information for many of the partner organizations, see this archived capture of the WDL site from 2021: https://www.loc.gov/item/lcwaN0018836/

This dataset includes structured data in several formats, representing the same descriptive metadata as translated between the seven languages:

Arabic (ar)
English (en)
Spanish (es)
French (fr)
Portuguese (pt)
Russian (ru)
Chinese (zh)

INCLUDED IN THIS DATASET:

The dataset is presented in multiple structured formats:

1. CSV file for each language, which includes all metadata fields and values.

	a. The field 'wdl_id' is the original WDL identifier and serves as a primary key between the data in the CSVs.

	b. Repeatable fields such as 'Additional Subjects' are separated by pipe characters ('|').

	c. The field 'title_in_original_language' is presented in the item's original language and script. All other fields are translated in the language of each CSV.

2. ZIP file for each language containing individual original metadata files in JSON and METS XML.

	a. The JSON includes all fieldnames translated into each of the 7 languages.
	
	b. The METS includes all fieldnames in English with translated metadata.
	
	c. Files are named by wdl_id.

HOW THIS DATASET WAS CREATED:

This dataset reflects the final state of metadata in WDL prior to the migration of most of the WDL items to loc.gov in 2021. The data was pulled from the WDL database and API into the multiple formats.

Any record updates or cataloging changes to these items after migration to loc.gov may not be reflected in this dataset.

For information on cataloging or questions about the items themselves, please refer to the loc.gov collection or to the providing institution.