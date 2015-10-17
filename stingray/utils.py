import numpy as np

def rebin_data(x, y, dx_new, method='sum'):

    """
    Rebin some data to an arbitrary new data resolution. Either sum
    the data points in the new bins or average them.

    Parameters:
    -----------
    x: iterable
        The dependent variable with some resolution dx_old = x[1]-x[0]

    y: interable
        The independent variable to be binned

    dx_new: float
        The new resolution of the dependent variable x

    method: {"sum" | "average" | "mean"}, optional, default "sum"
        The method to be used in binning. Either sum the samples y in
        each new bin of x, or take the arithmetic mean.


    Returns:
    --------
    xbin: numpy.ndarray
        The midpoints of the new bins in x

    ybin: numpy.ndarray
        The binned quantity y
    """

    dx_old = x[1] - x[0]
    step_size = np.float(dx_new)/np.float(dx_old)

    output = []
    for i in np.arange(0, y.shape[0], step_size):
        total = 0

        prev_frac = int(i+1) - i
        prev_bin = int(i)
        total += prev_frac * y[prev_bin]

        if i + step_size < len(x):
            # Fractional part of next bin:
            next_frac = i+step_size - int(i+step_size)
            next_bin = int(i+step_size)
            total += next_frac * y[next_bin]

        total += sum(y[int(i+1):int(i+step_size)])
        output.append(total)

    xbin = np.arange(len(output))*dx_new + x[0]
    if method in ['mean', 'avg', 'average', 'arithmetic mean']:
        ybin = np.array(output)/float(step_size)

    elif method == "sum":
        ybin = np.array(output)
    else:
        raise Exception("Method for summing or averaging not recognized. "
                        "Please enter either 'sum' or 'mean'.")

    return xbin, ybin