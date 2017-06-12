from scipy import sparse
import numpy as np

def slice_csr_rows(csr_matrix, mask, force_copy=False):
    '''Select and slice rows of a csr_matrix.

    Args:
        csr_matrix: A scipy.sparse.csr_matrix.
        mask: Either indices of the wanted rows or a mask.
        force_copy: Forces returning a copy if the mask is all the rows.

    Returns:
        A scipy.sparse.csr_matrix of the selected rows only.
    '''
    data = csr_matrix.data
    indices = csr_matrix.indices
    indptr = csr_matrix.indptr
    #decide whether `mask` is a mask or list of indices
    if np.size(mask)!=np.size(indptr)-1 or np.sum(mask)!=np.count_nonzero(mask):
        tmp = mask
        mask = np.zeros(np.size(indptr)-1, dtype=np.bool)
        mask[tmp] = True
    else:
        mask = mask.astype(np.bool)
    #indices of the rows to be deleted
    rows = np.arange(np.size(indptr)-1)[np.logical_not(mask)]
    if np.size(rows)==0:
        if force_copy:
            return csr_matrix.copy()
        else:
            return csr_matrix
    #copy the indices pointers
    ptrs = np.array(indptr)
    #get the elements' counts of those rows
    d_counts = [0]*np.size(rows)
    for i in range(len(rows)):
        d_counts[i] = ptrs[rows[i]+1]-ptrs[rows[i]]
        ptrs[rows[i]+1:] -= d_counts[i]
    #create the new arrays
    count = np.sum(d_counts)
    new_data = np.empty(np.size(data)-count, dtype=data.dtype)
    new_indices = np.empty(np.size(indices)-count, dtype=indices.dtype)
    new_indptr = np.empty(np.size(ptrs)-len(d_counts), dtype=ptrs.dtype)
    #fill new_indptr
    new_indptr[0] = 0 
    new_indptr[1:] = ptrs[1:][mask]
    #create a mask for data
    select = np.ones(np.size(data), dtype=np.bool)
    for i in range(len(rows)):
        idx = indptr[rows[i]]
        select[idx:idx+d_counts[i]] = False
    #fill new_data and new_indices
    new_data = data[select]
    new_indices = indices[select]
    new_shape = (csr_matrix.shape[0]-len(rows), csr_matrix.shape[1])
    return sparse.csr_matrix((new_data, new_indices, new_indptr), shape=new_shape)

def mask_csr_rows(csr_matrix, mask, force_copy=False):
    '''Zero out rows of a csr_matrix.

    This method doesn't change the size of the matrix.
    It only makes the rows zeros without considering them as part of the sparse structure.

    Args:
        csr_matrix: A scipy.sparse.csr_matrix.
        mask: Either indices of the wanted rows or a mask.
        force_copy: Forces deep cloning.

    Returns:
        A scipy.sparse.csr_matrix of the selected rows only.
    '''
    data = csr_matrix.data
    indices = csr_matrix.indices
    indptr = csr_matrix.indptr
    if force_copy:
        data = np.copy(data)
        indices = np.copy(indices)
        indptr = np.copy(indptr)

    #decide whether `mask` is a mask or list of indices
    if np.size(mask)!=np.size(indptr)-1 or np.sum(mask)!=np.count_nonzero(mask):
        tmp = mask
        mask = np.zeros(np.size(indptr)-1, dtype=np.bool)
        mask[tmp] = True
    #indices of the rows to be masked
    rows = np.arange(np.size(indptr)-1)[np.logical_not(mask)]
    #create the new arrays
    for i in range(len(rows)):
        data[indptr[rows[i]]:indptr[rows[i]+1]] = 0
    return sparse.csr_matrix((data, indices, indptr), shape=csr_matrix.shape)

if __name__=='__main__':
    data = np.array([1,1,3,1,5,5])
    indices = np.array([0,2,0,1,2,2])
    indptr = np.array([0,2,5,6])

    print('Original matrix')
    m = sparse.csr_matrix((data, indices, indptr))
    print(m.toarray())

    print('---------------------------------------')
    print('Mask: ', end='')
    mask = np.array([1,1,0])
    print(mask)
    
    print('Slice rows with the mask:')
    w = slice_csr_rows(m,mask, force_copy=True)
    print(w.toarray())

    print('Mask rows with the mask:')
    g = mask_csr_rows(m,mask, force_copy=True)
    print(g.toarray())

    print('---------------------------------------')
    print('Select rows: ',end='')
    rows = np.array([0,2])
    print(rows)

    print('Slice the selected rows:')
    w = slice_csr_rows(m,rows, force_copy=True)
    print(w.toarray())

    print('Mask with the selected rows:')
    g = mask_csr_rows(m,rows, force_copy=True)
    print(g.toarray())