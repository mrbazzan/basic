
(define (average a b)
  (/ (+ a b) 2)
)

(define (SQUARE_ROOT x)

  (define (IMPROVE guess)
    (average guess (/ x guess))
  )

  (define (GOOD_ENOUGH? guess)
    (< (abs (- x (square guess))) 0.0001)
  )

  (define (TRY guess)
    (if (GOOD_ENOUGH? guess)
	guess
	(TRY (IMPROVE guess))
    )
  )

  (TRY 1)
)
