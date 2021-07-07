import numpy as np

# NOTE: This code is not particularly 'good'. Can you make some improvements?
def conjugate_gradient(A, b, x_0):
    """
    A function to solve the linear system A x = b using the unpreconditioned
    conjugate gradient method.

    Parameters
    ----------
    A: ndarray
       Symmetric positive definite matrix
    b: ndarray
       The right-hand side of the linear system.
    x_0: ndarray
       An initial guess for the solution.

    Returns x, the solution of the linear system.
    """
    x = np.zeros_like(x_0)

    r = b - np.dot(A, x_0) # residual
    p = r
    rr_old = np.dot(r, r)

    # Guaranteed to converge with n iterations
    for i in range(0, b.shape[0]):
        Ap = A.dot(p)
        alpha = rr_old/np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap

        rr_new = np.dot(r, r)
        if np.sqrt(rr_new) < 1E-10:
            break

        p = r + (rr_new/rr_old)*p
        rr_old = rr_new

    return x

A = np.array([[4.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])
x_0 = np.zeros_like(b)
x = conjugate_gradient(A, b, x_0)
print(x)
assert(np.allclose(x, [1/11, 7/11]))
