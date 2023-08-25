
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


; atend 4 `(5 6 9)
; (cons 5 (cons 6 (cons 4 `())))

(define (atend x l)
  (if (null? l)
      (cons x l)
      (cons (car l) ( atend x (cdr l)) )
  )
)

