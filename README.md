# A Deep Dive into GPT-4's Data Mining Capabilities for Free-Text Spine Radiology Reports

We utilized GPT-4 for processing radiology reports with a single prompt. We classified the sentences into the spine and extraspine categories, determined the sentiment of each spine-related sentence and extracted the level of anatomy, anatomy and disorder triplets. 

We evaluated the method on two databases: 100 radiology spine reports from the MIMIC-III database and 53 radiology spine reports from the MTSamples collection. These results highlight how prompt-learning large language models can find information from free-text radiology reports without needing task-specific fine-tuning.

---

**OUTPUT:**

Extrapine sentences:

    - MRI of the brain is broadly within normal limits.

Positive sentiment sentences:

	- The cervical cord appears normal in its size and signal characteristics.
  	- At C4-5 and C5-6 there is no recurrent central or neural foraminal narrowing.
  	- Neither level demonstrates central or neural foraminal narrowing.
	- The C7-T1 level appears unremarkable.

Negative sentiment sentences:

	- The C2-3 and C3-4 discs are degenerated.
        - level: C2-3
        - anatomy: disc
        - degeneration: degenerated
        *****
        - level: C3-4
        - anatomy: disc
        - degeneration: degenerated
	- At C2-3 there is disc desiccation with a posterior central disc herniation.
        - level: C2-3
        - anatomy: disc
        - degeneration: desiccation
        *****
        - level: C2-3
        - anatomy: disc
        - degeneration: herniation
	- There is some mild bulging of the C3-4 disc.
        - level: C3-4
        - anatomy: disc
        - degeneration: bulging
	- At C6-7 there is mild bilateral bony neural foraminal narrowing without central canal compromise.
        - level: C6-7
        - anatomy: neural foramen
        - degeneration: narrowing
        
---
