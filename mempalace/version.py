"""Single source of truth for the MemPalace package version."""

# ⚠️ The "+pifork.N" is a PEP 440 LOCAL VERSION IDENTIFIER, and it is here for one
# reason: this is upstream/develop plus the pi-transcript sweeper port (see
# mempalace/sweeper.py), and without a local label the package reports plain
# "3.11.0" — indistinguishable from stock upstream. PEP 440 defines the label for
# exactly this: "fully API-compatible patched versions of upstream projects ...
# created by ... system integrators by applying specific backported bug fixes",
# whose purpose is to "differentiate upstream releases from potentially altered
# rebuilds by downstream integrators."
#
# ⚠️ Consequence, and it is deliberate: PEP 440 requires local labels to be IGNORED
# in version-specifier matching, so `mempalace>=3.11` cannot select the fork and
# stock upstream satisfies the same specifier. The label documents the build; it
# does not gate it. Bump N for each further fork revision.
__version__ = "3.11.0+pifork.1"
