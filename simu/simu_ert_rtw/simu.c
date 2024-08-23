/*
 * File: simu.c
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

#include "simu.h"

/* External inputs (root inport signals with default storage) */
ExtU_simu_T simu_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_simu_T simu_Y;

/* Real-time model */
static RT_MODEL_simu_T simu_M_;
RT_MODEL_simu_T *const simu_M = &simu_M_;

/* Model step function */
void simu_step(void)
{
  /* Outport: '<Root>/Out1' incorporates:
   *  Inport: '<Root>/In1'
   *  Inport: '<Root>/In2'
   *  Sum: '<S1>/Add'
   */
  simu_Y.Out1 = simu_U.In1 + simu_U.In2;
}

/* Model initialize function */
void simu_initialize(void)
{
  /* (no initialization code required) */
}

/* Model terminate function */
void simu_terminate(void)
{
  /* (no terminate code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
