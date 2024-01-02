# Title
> a brief summative of the proposed changes, e.g. "Added `Trait` trait. May be similar to the pull request title on GitHub (recommended)."

*NOTICE: Remove directions and examples (such as this one) when using this template*

## Summary of Changes[^r] 
> provide the overview of the changes being proposed, in bulleted form.
* Your list should define what is added/removed/revised.
    * Sub-lists should define *extending* additions/removals/revisions.
* *list here*

## Address(es)[^o]
> for additions/revisions/removals, that are coming from discussion(s) or other pull request(s).

*First, describe an overview; e.g. what was the disccusion about (also provide link)?*
*Second, provide the motive; e.g. why is [disccusion subject] important?*
*Third, describe your approach; e.g. how did you designed your codework?*
*Fourth, describe any and all tests and issues known (if applicable)*

## Time Complexity(ies)[^o]
> for additions or revisions that have functionalities, list/enumerate your function(s) and their corresponding time complexity(ies) with a short note following explaining the complexity. This section may not be added for traits and interfaces.

1. `Type::get_value()` - `O(1)`
    This is a valid note. Remember to note the whole stack of the function signature like `sublibrary::module::function()` or `function()` from `sublibrary::module`.
2. `sha256(...)` from `utils::hash::hash_method` - `O(n logn)`
    > This is also a valid (*but not prefered*) note. Overloaded functions that have the same time complexity should have their parameter list noted as `(...)`; overloads that deviate should be noted with their full parameter list.
3. *list here*

## Comparison(s)[^o]
> for revisions, tabulate in comparison points of revisions (as subsections).

### C1 `SampleItemRevised`

*define your revised item here; for functions and classes/structs, a note of the signature suffices. E.g. "`sample_sublibrary::sample_module::SampleItemRevised`"*

| Comparison Point | Current | Proposed / Revised |
| :--------------- | :-----: | :----------------: |
| Time Complexity  | `O(n)`  | `O(1)`             |

## Removal(s) and Replacement(s)[^o]
> for removals with/without replacement, list/enumerate items removed (with their replacements) with a note describing the motive of such change.

1. Removed prototype pull request template in `docs/CONTRIBUTING` (moved to `/` *repository root*)
    The template was not being recognized.
2. *list here*

## Known Issue(s) and Bug(s)[^o]
> for additions/revisions/removals, that have certain caveats or bugs encountered.

* *list here*

## Test(s)[^o]
> for additions/revisions/removals of functionalities, classes/structs and/or entire modules/sublibraries. Describe here also added testing if any.

* *list here*

## Note(s)[^o]
> Miscellaneous section for other details that might need to be raised.

* *list here*

[^r]: Required section(s)
[^o]: Optional section(s), quote under section for premise of requirement
