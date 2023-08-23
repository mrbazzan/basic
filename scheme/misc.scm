
(define (lastelement l)
  ( if (null? (cdr l))
       (car l)
       (lastelement (cdr l))
  )
)

(define (inlist x l)
  (if (null? l)
      #f
      (if (= (car l) x)
	  #t
	  (inlist x (cdr l))
      )
  )
)

