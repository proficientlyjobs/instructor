# Broken Links in Documentation

This file tracks all broken links found in the Instructor documentation during mkdocs build.

## Status Summary
- **Total Files with Issues**: 19
- **Total Broken Links**: ~70+
- **Main Issue**: Incorrect path depth (`../../../` should be `../../`)

## By File

### blog/posts/best_framework.md
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`
- [ ] Fix `../../../concepts/parallel.md` → `../../concepts/parallel.md`
- [ ] Fix `../../../concepts/partial.md` → `../../concepts/partial.md`
- [ ] Fix `../../../concepts/iterable.md` → `../../concepts/iterable.md`
- [ ] Fix `../../../concepts/types.md` → `../../concepts/types.md`
- [ ] Fix `../../../concepts/unions.md` → `../../concepts/unions.md`
- [ ] Fix `../../../integrations/together.md` → `../../integrations/together.md`
- [ ] Fix `../../../integrations/ollama.md` → `../../integrations/ollama.md`
- [ ] Fix `../../../integrations/groq.md` → `../../integrations/groq.md`
- [ ] Fix `../../../integrations/llama-cpp-python.md` → `../../integrations/llama-cpp-python.md`
- [ ] Fix `../../../concepts/philosophy.md` → `../../concepts/philosophy.md`
- [ ] Fix `../../../concepts/patching.md` → `../../concepts/patching.md`

### blog/posts/caching.md
- [ ] Fix unrecognized relative link `../../examples/caching/`
- [ ] Fix `../../../concepts/partial.md` → `../../concepts/partial.md`
- [ ] Fix `../../../concepts/caching.md` → `../../concepts/caching.md`
- [ ] Fix `../../../concepts/prompt_caching.md` → `../../concepts/prompt_caching.md`
- [ ] Fix `../../../concepts/parallel.md` → `../../concepts/parallel.md`
- [ ] Fix `../../../concepts/dictionary_operations.md` → `../../concepts/dictionary_operations.md`

### blog/posts/chat-with-your-pdf-with-gemini.md
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`

### blog/posts/extracting-model-metadata.md
- [ ] Fix `../../../concepts/multimodal.md` → `../../concepts/multimodal.md`

### blog/posts/generator.md
- [ ] Fix `../../../concepts/fastapi.md` → `../../concepts/fastapi.md`

### blog/posts/google-openai-client.md
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`

### blog/posts/introducing-structured-outputs.md
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`
- [ ] Fix `../../../concepts/lists.md` → `../../concepts/lists.md`
- [ ] Fix `../../../concepts/partial.md` → `../../concepts/partial.md`

### blog/posts/introduction.md
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`
- [ ] Fix `../../../concepts/models.md` → `../../concepts/models.md`

### blog/posts/learn-async.md
- [ ] Fix `../../../concepts/error_handling.md` → `../../concepts/error_handling.md`
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`

### blog/posts/native_caching.md
- [ ] Fix `../../../concepts/caching.md` → `../../concepts/caching.md` (appears twice)

### blog/posts/open_source.md
- [ ] Fix `../../../concepts/patching.md#json-mode` → `../../concepts/patching.md#json-mode`
- [ ] Fix `../../../integrations/llama-cpp-python.md` → `../../integrations/llama-cpp-python.md`
- [ ] Fix `../../../concepts/patching.md` → `../../concepts/patching.md`
- [ ] Fix `../../../integrations/ollama.md` → `../../integrations/ollama.md`
- [ ] Fix `../../../integrations/groq.md` → `../../integrations/groq.md`
- [ ] Fix `../../../integrations/together.md` → `../../integrations/together.md`
- [ ] Fix `../../../integrations/mistral.md` → `../../integrations/mistral.md`

### blog/posts/openai-multimodal.md
- [ ] Fix `../../../integrations/openai.md` → `../../integrations/openai.md`

### blog/posts/pydantic-is-still-all-you-need.md
- [ ] Fix `../../../concepts/models.md` → `../../concepts/models.md`
- [ ] Fix `../../../integrations/ollama.md` → `../../integrations/ollama.md`
- [ ] Fix `../../../integrations/llama-cpp-python.md` → `../../integrations/llama-cpp-python.md`
- [ ] Fix `../../../integrations/anthropic.md` → `../../integrations/anthropic.md`
- [ ] Fix `../../../integrations/cohere.md` → `../../integrations/cohere.md`
- [ ] Fix `../../../integrations/google.md` → `../../integrations/google.md`
- [ ] Fix `../../../integrations/vertex.md` → `../../integrations/vertex.md`
- [ ] Fix `../../../concepts/partial.md` → `../../concepts/partial.md` (appears twice)
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`

### blog/posts/semantic-validation-structured-outputs.md
- [ ] Fix `../../concepts/llm_validation.md` → file does not exist, need to check if should be different file or create it

### blog/posts/structured-output-anthropic.md
- [ ] Fix `../../../integrations/anthropic.md` → `../../integrations/anthropic.md`

### blog/posts/using_json.md
- [ ] Fix `../../../integrations/together.md` → `../../integrations/together.md`
- [ ] Fix `../../../integrations/ollama.md` → `../../integrations/ollama.md`
- [ ] Fix `../../../integrations/llama-cpp-python.md` → `../../integrations/llama-cpp-python.md`
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`
- [ ] Fix `../../../concepts/lists.md` → `../../concepts/lists.md`
- [ ] Fix `../../../concepts/partial.md` → `../../concepts/partial.md`

### blog/posts/version-1.md
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`
- [ ] Fix `../../../concepts/reask_validation.md` → `../../concepts/reask_validation.md`

### blog/posts/youtube-flashcards.md
- [ ] Fix `../../../concepts/retrying.md` → `../../concepts/retrying.md`

### integrations/truefoundry.md
- [ ] Fix absolute link `/gateway/authentication` → should be relative or external URL

### blog/posts/announcing-instructor-responses-support.md
- [ ] Fix missing anchor `../../integrations/openai.md#responses` → anchor doesn't exist in target file

## Missing Navigation Pages
These files exist but are not included in the navigation configuration:
- [ ] Add `AGENT.md` to nav
- [ ] Add `concepts/batch.md` to nav
- [ ] Add `examples/batch_classification_langsmith.md` to nav
- [ ] Add `examples/batch_in_memory.md` to nav
- [ ] Add `examples/batch_job_oai.md` to nav

## Bulk Fix Commands

### Fix all triple-dot paths to double-dot:
```bash
find docs/blog/posts/ -name "*.md" -exec sed -i '' 's|\.\./\.\./\.\./|../../|g' {} \;
```

### Fix specific non-existent files:
- Check if `concepts/llm_validation.md` should exist or be renamed
- Check if `integrations/openai.md` has `#responses` anchor

## Notes
- Most issues are caused by incorrect relative path depth (`../../../` instead of `../../`)
- Blog posts are at `docs/blog/posts/` so they need `../../` to reach `docs/`
- Some files may need anchor creation or link target verification
- TrueFoundry link may be intentionally external

## Progress
- [x] Identified all broken links
- [x] Categorized by file and issue type
- [ ] Execute bulk path fixes
- [ ] Handle special cases individually
- [ ] Verify all fixes work
- [ ] Update navigation for missing pages