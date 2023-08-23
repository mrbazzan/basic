
(define (lastelement l)
  ( if (null? (cdr l))
       (car l)
       (lastelement (cdr l))
  )
)
