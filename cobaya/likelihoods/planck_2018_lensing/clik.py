from cobaya.likelihoods._base_classes import planck_clik


class clik(planck_clik):
    r"""
    Lensing likelihood of Planck's 2018 data release based on temperature+polarization
    map-based lensing reconstruction \cite{Aghanim:2018oex}.
    """
    bibtex_file = 'PlanckLensing2018.bibtex'
