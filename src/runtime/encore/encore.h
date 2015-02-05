#ifndef ENCORE_H_6Q243YHL
#define ENCORE_H_6Q243YHL

static pony_type_t *ENCORE_ACTIVE    = (pony_type_t *)1;
static pony_type_t *ENCORE_PRIMITIVE = (pony_type_t *)NULL;

typedef struct encore_actor encore_actor_t;
typedef struct encore_oneway_msg encore_oneway_msg_t;
typedef struct encore_fut_msg encore_fut_msg_t;

typedef union
{
  void* p;
  intptr_t i;
  double d;
} encore_arg_t;

typedef enum {
  ID_CLOSURE = 0,
  ID_FUTURE,
  ID_SCONS,
} encore_type_id;

typedef enum {
  _ENC__MSG_RESUME_GET, /// This should probably go
  _ENC__MSG_RESUME_SUSPEND,
  _ENC__MSG_RESUME_AWAIT,
  _ENC__MSG_RUN_CLOSURE,
  _ENC__MSG_MAIN,
} encore_msg_id;

struct encore_oneway_msg
{
  struct pony_msg_t;
};

#include "future.h"

struct encore_fut_msg
{
  encore_oneway_msg_t;
  future_t    *_fut;
};

struct encore_actor
{
  pony_actor_pad_t;
  // Everything else that goes into an encore_actor that's not part of PonyRT
};

/// Create a new Encore actor
encore_actor_t *encore_create(pony_type_t *type);

/// Allocate s bytes of memory, zeroed out
void *encore_alloc(size_t s);

/// The starting point of all Encore programs
int encore_start(int argc, char** argv, pony_type_t *type);

#endif /* end of include guard: ENCORE_H_6Q243YHL */
