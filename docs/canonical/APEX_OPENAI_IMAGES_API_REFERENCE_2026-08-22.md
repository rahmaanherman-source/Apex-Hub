# APEX OPENAI IMAGES API REFERENCE — 2026-08-22

**STATUS:** CANONICAL STAGING / SOURCE-INGESTED
**AUTHORITY:** APEX-Laws
**OWNER:** Apex-Hub cross-repository integration map
**SOURCE BASIS:** User-supplied OpenAI Images API reference material in the APEX audit feed.
**VERIFICATION STATE:** Source-ingested. Treat availability, model names, limits, and parameter details as requiring current official-source verification before promotion to independently verified platform truth.

## 1. Scope

This reference records the OpenAI image capabilities that APEX must consider before building duplicate image-generation or image-editing infrastructure.

The API surfaces supplied in the source are:

- `POST /images/variations`
- `POST /images/edits`
- `POST /images/generations`

The source describes image generation from a prompt and/or input image, image editing, image references, masks, streaming, partial-image events, output controls, usage telemetry, and image model identifiers.

## 2. Capability Matrix

| Capability | API surface | Source status |
|---|---|---|
| Create image from prompt | `/images/generations` | Documented |
| Edit existing image | `/images/edits` | Documented |
| Use one or more source images | `/images/edits` | Documented; source states up to 16 images for GPT Image models |
| Masked image editing | `/images/edits` + `mask` | Documented |
| Image variation | `/images/variations` | Documented; supplied source states DALL-E 2 only |
| URL image input | edit/reference workflow | Documented |
| Base64 data URL image input | edit/reference workflow | Documented |
| File ID image input | edit/reference workflow | Documented |
| Transparent background | GPT Image generation/edit | Documented where supported |
| PNG output | generation/edit | Documented |
| JPEG output | generation/edit | Documented |
| WebP output | generation/edit | Documented |
| Low/medium/high quality | GPT Image | Documented |
| Auto quality | GPT Image | Documented |
| Auto size | supported GPT Image workflows | Documented |
| Streaming | generation/edit | Documented |
| Partial image events | generation/edit | Documented; source specifies 0–3 |
| Usage telemetry | GPT Image | Documented |
| End-user identifier | `user` | Documented |

## 3. Image Edit Contract

`POST /images/edits` accepts one or more source image references and a prompt. The supplied source describes the following input image reference forms:

- `file_id`
- fully qualified `image_url`
- base64-encoded data URL through `image_url`

The source also describes an optional mask. A mask must be supplied by `file_id` or `image_url`, with exactly one of those fields used for the mask reference.

The source describes the following edit controls:

- `background`: `transparent`, `opaque`, or `auto`
- `input_fidelity`: `high` or `low` where supported by the selected model/documentation
- `model`
- `moderation`: `low` or `auto`
- `n`
- `output_compression`
- `output_format`: `png`, `jpeg`, `webp`
- `partial_images`: `0` through `3`
- `quality`: `low`, `medium`, `high`, `auto`
- `size`: `auto`, `1024x1024`, `1536x1024`, `1024x1536`
- `stream`
- `user`

## 4. Mask Requirements

The supplied source states:

1. The image and mask must use the same format and size.
2. The image and mask must remain below the documented file-size limit.
3. The mask must contain an alpha channel.
4. When multiple input images are supplied, the mask applies to the first image.
5. Masking is guidance rather than a guarantee of pixel-perfect boundary adherence.

APEX therefore records three separate states:

```text
REQUESTED REGION
≠ MODEL EDIT RESULT
≠ VERIFIED REGION PRESERVATION
```

## 5. Image Generation Contract

`POST /images/generations` creates image output from a prompt.

The supplied reference describes these controls:

- `prompt`
- `background`
- `model`
- `moderation`
- `n`
- `output_compression`
- `output_format`
- `partial_images`
- `quality`
- `response_format` for legacy DALL-E URL/base64 workflows
- `size`
- `stream`
- `style` for DALL-E 3
- `user`

The source describes GPT Image models and legacy DALL-E models separately. APEX must not collapse legacy and current model behavior into one unqualified capability claim.

## 6. Image Variation

`POST /images/variations` creates a variation from an input image.

The supplied reference explicitly states that this endpoint supports DALL-E 2 only. APEX should therefore treat this as a legacy/specialized capability and prefer the current image-edit/reference workflow when that is the appropriate supported path.

## 7. Image Models

The supplied source lists:

- `gpt-image-1.5`
- `gpt-image-2`
- `gpt-image-2-2026-04-21`
- `dall-e-2`
- `dall-e-3`
- `gpt-image-1`
- `gpt-image-1-mini`

Model availability and exact feature support must be verified against the current official model documentation and target account before production routing.

## 8. Output Artifact Types

### Image

The supplied source defines an Image object with:

- `b64_json`
- `revised_prompt` for DALL-E 3
- `url` for DALL-E 2/DALL-E 3 URL workflows

GPT Image workflows return base64 image data rather than the legacy temporary URL behavior described for DALL-E.

### ImagesResponse

The source describes:

- `created`
- `background`
- `data`
- `output_format`
- `quality`
- `size`
- `usage`

## 9. Streaming Event Contract

### Image edit

`ImageEditStreamEvent = ImageEditPartialImageEvent | ImageEditCompletedEvent`

Partial event fields include:

- `b64_json`
- `background`
- `created_at`
- `output_format`
- `partial_image_index`
- `quality`
- `size`
- `type = image_edit.partial_image`

Completed event fields include:

- `b64_json`
- `background`
- `created_at`
- `output_format`
- `quality`
- `size`
- `type = image_edit.completed`
- `usage`

### Image generation

`ImageGenStreamEvent = ImageGenPartialImageEvent | ImageGenCompletedEvent`

Partial event fields include:

- `b64_json`
- `background`
- `created_at`
- `output_format`
- `partial_image_index`
- `quality`
- `size`
- `type = image_generation.partial_image`

Completed event fields include:

- `b64_json`
- `background`
- `created_at`
- `output_format`
- `quality`
- `size`
- `type = image_generation.completed`
- `usage`

## 10. Usage Telemetry

For GPT Image workflows, the supplied source describes usage fields including:

- `input_tokens`
- `input_tokens_details.image_tokens`
- `input_tokens_details.text_tokens`
- `output_tokens`
- `total_tokens`
- `output_tokens_details.image_tokens`
- `output_tokens_details.text_tokens` where returned by the specific response type

APEX should preserve this telemetry as runtime evidence where available. Cost calculations should use current official pricing rather than hard-coded historical values.

## 11. APEX Routing Rule

Do not build a duplicate image engine when the approved OpenAI capability satisfies the requirement.

```text
USER / GABBY INTENT
        ↓
CAPABILITY REGISTRY
        ↓
APPROVED IMAGE ROUTE
        ↓
OPENAI IMAGE GENERATION / EDIT
        ↓
RUNTIME ARTIFACT
        ↓
VERIFICATION
        ↓
VERSION / PROVENANCE / ARCHIVE
```

AI output is not automatically verified truth.

## 12. Character Studio Use Cases

The recorded capabilities support these candidate APEX workflows:

- text-to-character concept generation;
- reference-image character generation;
- clothing and accessory edits;
- localized masked edits;
- environment/background generation;
- multi-reference composition;
- transparent asset generation where supported;
- iterative edits;
- streaming preview;
- asset versioning and provenance capture.

These are capability mappings, not claims that every workflow is already implemented in APEX Terminal.

## 13. Capability Registry Record

Recommended registry record shape:

```yaml
provider: OpenAI
capability_family: images
status: Researching
confidence: source_ingested
nativeSupport: false
pluginSupport: false
restSupport: true
sdkSupport: true
partnerSupport: false
buildRequired: false
endpoints:
  - POST /images/generations
  - POST /images/edits
  - POST /images/variations
models:
  - gpt-image-1.5
  - gpt-image-2
  - gpt-image-2-2026-04-21
  - gpt-image-1
  - gpt-image-1-mini
  - dall-e-2
  - dall-e-3
evidenceLevel: user_supplied_official_docs
lastTested: null
verificationRequired: true
```

Do not mark this record `Production` or `Verified` solely from documentation.

## 14. No-Fake-Green Promotion Gate

Promotion requires:

`DOCUMENTED → CONFIGURED → CONNECTED → EXECUTED → TESTED → VERIFIED`

Before independent verification:

1. Read current official OpenAI documentation.
2. Confirm model and endpoint availability.
3. Confirm current SDK/schema behavior.
4. Test generation, edit, reference, mask, and streaming paths as applicable.
5. Capture runtime evidence.
6. Record failures, limits, cost, and latency where material.
7. Update the Capability Registry.
8. Promote only claims supported by evidence.

**NO FALSE GREEN.**
