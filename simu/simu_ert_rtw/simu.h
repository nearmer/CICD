/*
 * File: simu.h
 *
 * Code generated for Simulink model 'simu'.
 *
 * Model version                  : 1.6
 * Simulink Coder version         : 9.9 (R2023a) 19-Nov-2022
 * C/C++ source code generated on : Fri Jun  2 18:26:56 2023
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_simu_h_
#define RTW_HEADER_simu_h_
#ifndef simu_COMMON_INCLUDES_
#define simu_COMMON_INCLUDES_
#include "rtwtypes.h"
#endif                                 /* simu_COMMON_INCLUDES_ */

#include "simu_types.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* External inputs (root inport signals with default storage) */
typedef struct {
  real_T In1;                          /* '<Root>/In1' */
  real_T In2;                          /* '<Root>/In2' */
} ExtU_simu_T;

/* External outputs (root outports fed by signals with default storage) */
typedef struct {
  real_T Out1;                         /* '<Root>/Out1' */
} ExtY_simu_T;

/* Real-time Model Data Structure */
struct tag_RTM_simu_T {
  const char_T * volatile errorStatus;
};

/* External inputs (root inport signals with default storage) */
extern ExtU_simu_T simu_U;

/* External outputs (root outports fed by signals with default storage) */
extern ExtY_simu_T simu_Y;

/* Model entry point functions */
extern void simu_initialize(void);
extern void simu_step(void);
extern void simu_terminate(void);

/* Real-time Model object */
extern RT_MODEL_simu_T *const simu_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'simu'
 * '<S1>'   : 'simu/Subsystem'
 */
#endif                                 /* RTW_HEADER_simu_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
